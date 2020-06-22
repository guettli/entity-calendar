import datetime

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.urls import reverse


class Entity(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

    def day_is_in_one_range(self, day):
        return TimeRangeOfEntity.objects.filter(entity=self, start__lte=day, end__gte=day).exists()

    def get_absolute_url(self):
        return reverse('admin:entity_calendar_entity_change', args=(self.id,))

class StartEndModel(models.Model):
    start = models.DateField()
    end = models.DateField()
    class Meta:
        abstract = True
    def clean(self):
        super()
        if not self.start:
            return
        if not self.end:
            return
        if self.start>self.end:
            raise ValidationError('start must be smaller or equal end: {} {}'.format(self.start, self.end))

class TimeRangeOfEntity(StartEndModel):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

class PeriodList(models.Model):
    """
    Example: 2020 Quarter 1
    """
    name = models.CharField(max_length=1024)
    def __str__(self):
        return self.name

class Period(StartEndModel):
    """
    Example: Sprint Q1/1
    """
    name = models.CharField(max_length=1024)
    period_list = models.ForeignKey(PeriodList, on_delete=models.CASCADE, related_name='periods')
    def __str__(self):
        return self.name


class PeriodsAndEntitiesView(models.Model):
    """
    Example: 2020-Quarter1
    """
    name = models.CharField(max_length=1024)
    entities = models.ManyToManyField(Entity)
    period_list = models.ForeignKey(PeriodList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('period_and_entity_view', kwargs=dict(pk=self.pk))

    def days(self):
        days=[]
        for period in self.period_list.periods.order_by('start'):
            current = period.start
            assert period.start <= period.end
            is_first = True
            while current<=period.end:
                days.append((current, is_first))
                is_first = False
                current += datetime.timedelta(days=1)
        return days