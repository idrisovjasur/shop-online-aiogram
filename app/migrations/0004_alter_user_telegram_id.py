# Generated by Django 4.2 on 2023-05-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(),
        ),
    ]
