# Generated by Django 5.1.2 on 2024-11-15 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0013_checkeddata_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkeddata',
            name='ip_address',
        ),
    ]
