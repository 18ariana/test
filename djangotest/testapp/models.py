from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.postgres.fields import JSONField


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, verbose_name="логин")
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход', auto_now_add=True)
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_valid = models.BooleanField(default=False, verbose_name='Подтвержденный email')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Необходимо ввести имя пользователя')

        if not email:
            raise ValueError('Необходимо ввести адрес электронной почты')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Флаг is_staff для суперпользователя должен быть True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Флаг is_superuser для суперпользователя должен быть True.')

        return self._create_user(username, email, password, **extra_fields)


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, db_index=True, related_name="profile")
    first_name = models.CharField(verbose_name="Имя", max_length=60, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=60, blank=True)
    middle_name = models.CharField(verbose_name="Отчество", max_length=60, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", null=True, blank=True, unique=True)
    links = models.CharField(verbose_name="Ссылки", max_length=255, blank=True)
    json = JSONField(verbose_name="JSON'ы", blank=True, null=True)


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=MyUser)
