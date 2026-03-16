# Data migration: default FAQ items

from django.db import migrations


def create_default_faq(apps, schema_editor):
    FAQItem = apps.get_model('main', 'FAQItem')
    defaults = [
        (0, 'Как вы заботитесь о моем здоровье?',
         'Мы сотрудничаем только с аккредитованными клиниками и лучшими репродуктологами. '
         'Вы проходите тщательный скрининг, а во время программы мы обеспечиваем лучшее питание, '
         'витамины и постоянный медицинский контроль. Ваше здоровье — наш приоритет №1.'),
        (1, 'Нужно ли мне будет уезжать от семьи?',
         'Для донорства яйцеклеток требуется короткий визит (около 10-12 дней). '
         'Для суррогатного материнства возможен переезд в Тбилиси или Бишкек на время беременности, '
         'где мы предоставляем комфортное жилье, где вы сможете находиться со своими детьми.'),
        (2, 'Это законно и безопасно?',
         'Абсолютно. В Грузии и Кыргызстане суррогатное материнство и донорство полностью легальны. '
         'Мы оформляем нотариально заверенные договора, которые защищают ваши права и гарантируют '
         'выплату вознаграждения в полном объеме.'),
    ]
    for order, question, answer in defaults:
        FAQItem.objects.get_or_create(
            question=question,
            defaults={'answer': answer, 'order': order},
        )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_faq, noop),
    ]
