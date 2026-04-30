# Обновление текстов FAQ и устранение дубликатов отзывов в Story

from django.db import migrations


ELENA_TESTIMONIAL = (
    'Для меня это не было просто процедурой. Это был момент, когда я поняла, '
    'что могу изменить чью-то жизнь. В Sunrise Family меня встретили как родную. '
    'Весь процесс прошел в атмосфере полного доверия.'
)

MARIA_TESTIMONIAL = (
    'Благодаря программе я не только помогла прекрасной паре, но и обеспечила '
    'будущее своим детям. Кураторы в Тбилиси стали для меня почти семьей. '
    'Никаких тревог, только поддержка.'
)


def update_faq_and_stories(apps, schema_editor):
    FAQItem = apps.get_model('main', 'FAQItem')
    Story = apps.get_model('main', 'Story')

    faq_updates = {
        'Как вы заботитесь о моем здоровье?': (
            'Мы подключаем клиники и врачей в рамках вашей программы: проходите '
            'скрининг, получаете наблюдение по клиническим протоколам и '
            'рекомендации специалистов. Быт, питание и сопровождение между '
            'визитами мы согласовываем заранее, чтобы вам было спокойнее.'
        ),
        'Нужно ли мне будет уезжать от семьи?': (
            'Для донорства яйцеклеток обычно нужен короткий визит (около 10–12 дней). '
            'Для суррогатного материнства возможен переезд в Тбилиси или Бишкек на '
            'время беременности: мы помогаем с жильём и организацией быта так, '
            'чтобы вы могли оставаться рядом с детьми, если это входит в ваш маршрут.'
        ),
        'Это законно и безопасно?': (
            'В Грузии и Кыргызстане суррогатное материнство и донорство '
            'регулируются законом. Мы оформляем нотариально заверенные договоры: '
            'в них прописаны условия программы, в том числе порядок и сроки '
            'выплат по вознаграждению — чтобы вы понимали свои шаги заранее.'
        ),
    }
    for question, answer in faq_updates.items():
        FAQItem.objects.filter(question=question).update(answer=answer)

    # Два отзыва с одним и тем же текстом — оставляем еленин для донора, для сурмамы — отдельный.
    stories = list(Story.objects.order_by('order', 'id'))
    if len(stories) >= 2:
        first_txt = (stories[0].testimonial or '').strip()
        second_txt = (stories[1].testimonial or '').strip()
        if first_txt and first_txt == second_txt:
            stories[1].testimonial = MARIA_TESTIMONIAL
            stories[1].save(update_fields=['testimonial'])

    for story in Story.objects.exclude(role__iexact='').iterator():
        role_l = story.role.strip().lower()
        if any(x in role_l for x in ('сур', 'сурмама', 'суррогат')):
            if (story.testimonial or '').strip() == ELENA_TESTIMONIAL.strip():
                story.testimonial = MARIA_TESTIMONIAL
                story.save(update_fields=['testimonial'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_application_message'),
    ]

    operations = [
        migrations.RunPython(update_faq_and_stories, noop),
    ]
