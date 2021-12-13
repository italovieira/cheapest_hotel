from collections import Counter
from datetime import datetime
from typing import Iterable

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.expressions import F


class HotelManager(models.Manager):
    def cheapest(self, client: str, dates: Iterable[datetime]) -> str:
        count = Counter()
        for date in dates:
            if date.weekday() < 5:
                count['weekday'] += 1
            else:
                count['weekend'] += 1

        return self.annotate(
            cost=F(f'weekday_{client}_tax') * count['weekday'] +
                 F(f'weekend_{client}_tax') * count['weekend']
        ).order_by('cost', '-rating').first().name


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField(
                validators=(MinValueValidator(1), MaxValueValidator(5)))
    weekend_regular_tax = models.FloatField()
    weekend_reward_tax = models.FloatField()
    weekday_regular_tax = models.FloatField()
    weekday_reward_tax = models.FloatField()
    objects = HotelManager()
