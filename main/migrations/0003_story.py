# Generated migration for Story model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_data_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('role', models.CharField(help_text='Например: донор, сурмама', max_length=100, verbose_name='Роль')),
                ('tagline', models.CharField(help_text='Короткая фраза в кавычках', max_length=300, verbose_name='Краткая цитата')),
                ('testimonial', models.TextField(verbose_name='Текст отзыва')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='stories/', verbose_name='Фото')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
                'ordering': ['order'],
            },
        ),
    ]
