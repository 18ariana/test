# Generated by Django 3.0.4 on 2020-10-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_delete_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_valid',
            field=models.BooleanField(default=False, verbose_name='Подтвержденный email'),
        ),
    ]
