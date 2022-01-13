from django.db import models

# Create your models here.

PARTY_SIZES = [
    (1,"1"),
    (2, "2"),
    (4, "3"),
    (6, "4"),
    (8 , "8")
]


class Table(models.Model):
    party_size = models.IntegerField(choices=PARTY_SIZES)
    available_date = models.DateField()

    def __str__(self):
        return f"Table Number {self.id}"
    