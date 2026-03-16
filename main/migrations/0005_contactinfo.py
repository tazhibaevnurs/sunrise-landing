# Generated migration for ContactInfo model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_story_default_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('address_1', models.CharField(blank=True, help_text='Например: Тбилиси, Грузия', max_length=255, verbose_name='Адрес 1')),
                ('address_2', models.CharField(blank=True, help_text='Например: Бишкек, Кыргызстан', max_length=255, verbose_name='Адрес 2')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('footer_description', models.TextField(blank=True, help_text='Текст под логотипом в подвале', verbose_name='Описание в футере')),
                ('copyright_text', models.CharField(blank=True, help_text='Например: © 2016 - 2026 Sunrise Family • Сделано с любовью и заботой о жизни', max_length=255, verbose_name='Текст копирайта')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
            },
        ),
    ]
