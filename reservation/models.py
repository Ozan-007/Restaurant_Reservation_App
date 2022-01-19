from asyncore import write
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PARTY_SIZES = [
    ("1","1"),
    ("2", "2"),
    ("4", "3"),
    ("6", "4"),
    ("8" , "8")
]


class Table(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,default= None)
    party_size = models.CharField(max_length=1, choices=PARTY_SIZES)
    available_date = models.DateField()

    def __str__(self):
        return f"Table Number {self.id}"
    