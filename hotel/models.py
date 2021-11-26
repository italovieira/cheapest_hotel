from django.db import models
from django.core.validators import  MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField(
                validators=(MinValueValidator(1), MaxValueValidator(5)))
    weekend_regular_tax = models.FloatField()
    weekend_reward_tax = models.FloatField()
    weekday_regular_tax = models.FloatField()
    weekday_reward_tax = models.FloatField()
