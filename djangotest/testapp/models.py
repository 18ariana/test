from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.IntegerField("Age")
    telephone = models.CharField("Telephone", max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"
