from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_application_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='message',
        ),
    ]
