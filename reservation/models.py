from django.db import models

# Create your models here.

PARTY_SIZES = [
    (2, 1),
    (3,4),
    (5, 6),
]


class Table(models.Model):
    party_size = models.IntegerField(choices=PARTY_SIZES)
    available_date = models.DateField()
    available_time = models.TimeField()

    def __str__(self):
        return f"Table Number {self.id}"
    