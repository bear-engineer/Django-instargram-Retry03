# Generated by Django 2.0.6 on 2018-06-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180627_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
