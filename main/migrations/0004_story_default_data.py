# Data migration: default stories (Elena, Maria)

from django.db import migrations


def create_default_stories(apps, schema_editor):
    Story = apps.get_model('main', 'Story')
    if Story.objects.exists():
        return
    Story.objects.bulk_create([
        Story(
            name='Елена',
            role='донор',
            tagline='Помогла обрести счастье другим',
            testimonial='Для меня это не было просто процедурой. Это был момент, когда я поняла, что могу изменить чью-то жизнь. В Sunrise Family меня встретили как родную. Весь процесс прошел в атмосфере полного доверия.',
            order=0,
        ),
        Story(
            name='Мария',
            role='сурмама',
            tagline='Чувствовала заботу на каждом шагу',
            testimonial='Благодаря программе я не только помогла прекрасной паре, но и обеспечила будущее своим детям. Кураторы в Тбилиси стали для меня почти семьей. Никаких тревог, только поддержка.',
            order=1,
        ),
    ])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_story'),
    ]

    operations = [
        migrations.RunPython(create_default_stories, noop),
    ]
