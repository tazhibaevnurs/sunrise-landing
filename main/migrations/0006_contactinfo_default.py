# Data migration: one default ContactInfo with template data

from django.db import migrations


def create_default_contact(apps, schema_editor):
    ContactInfo = apps.get_model('main', 'ContactInfo')
    if ContactInfo.objects.exists():
        return
    ContactInfo.objects.create(
        phone='+7 (900) 000-00-00',
        address_1='Тбилиси, Грузия',
        address_2='Бишкек, Кыргызстан',
        footer_description='Лицензированное агентство репродуктивной помощи. Мы объединяем сердца и создаем будущее с 2016 года.',
        copyright_text='© 2016 - 2026 Sunrise Family • Сделано с любовью и заботой о жизни',
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_contactinfo'),
    ]

    operations = [
        migrations.RunPython(create_default_contact, noop),
    ]
