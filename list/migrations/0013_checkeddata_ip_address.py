# Generated by Django 5.1.2 on 2024-11-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0012_alter_checkeddata_check_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkeddata',
            name='ip_address',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
