# Generated by Django 3.0.4 on 2020-10-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200930_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='логин')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='Последний вход')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Сотрудник')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Суперпользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
