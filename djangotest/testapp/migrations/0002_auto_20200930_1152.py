# Generated by Django 3.0.4 on 2020-09-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Human', 'verbose_name_plural': 'People'},
        ),
    ]
