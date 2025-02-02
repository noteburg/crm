from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL, Model


# Create your models here.

class Filial(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} in {self.region}"


class Employee(AbstractUser):
    phone = models.CharField(max_length=25)
    role = models.CharField(
        choices=(
            ('0', 'director'),
            ('1', 'administrator'),
            ('2', 'bugalter'),
            ('3', 'teacher'),

        ),  default='3', max_length=10)

    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField(default=True)

class CleanerEmployee(models.Model):
    first_name = models.CharField(255)
    last_name = models.CharField(255)
    phone = models.CharField(max_length=25)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    @property
    def role(self):
        return "cleaner"
