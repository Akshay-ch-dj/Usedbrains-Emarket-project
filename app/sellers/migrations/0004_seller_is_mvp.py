# Generated by Django 3.1.1 on 2020-09-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0003_auto_20200911_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]