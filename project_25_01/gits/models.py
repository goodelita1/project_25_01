from typing import Any
from django.conf import settings
from django.db import models

# Create your models here.
class HashInfoModel(models.Model):
    hash_name = models.CharField(max_length=20)
    complexity_brut = models.IntegerField(max_length=20)
    edition_year = models.DateField()
    when_used = models.DateTimeField()
    military = models.BooleanField()


    def __str__(self) -> str:
        return self.hash_name

class ImplantInfoModel(models.Model):
    TYPE_CHOICES = (
    ("IMPOSSIBLE", "im"),
    ("DIFFICULT", "df"),
    ("MIDDLE", "md"),
    ("EASY", "ez"),
)
    implant_name = models.CharField(max_length=20)
    buy_possibility = models.CharField(max_length=20,
                  choices=TYPE_CHOICES)
    strange_type = models.CharField(max_length=20,
                  choices=TYPE_CHOICES)
    defense = models.IntegerField(max_length=20)

    def __str__(self) -> str:
        return self.implant_name
