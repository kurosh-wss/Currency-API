# Generated by Django 3.2 on 2021-11-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_api_call_apicall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='get_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
