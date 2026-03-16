# Add message field and meeting type support

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contactinfo_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='message',
            field=models.TextField(blank=True, verbose_name='Сообщение / комментарий'),
        ),
    ]
