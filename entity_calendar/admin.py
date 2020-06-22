from django.contrib import admin

# Register your models here.
from entity_calendar.models import TimeRangeOfEntity, Entity, Period, PeriodList, PeriodsAndEntitiesView


class TimeRageInline(admin.TabularInline):
    model = TimeRangeOfEntity
    ordering = ('start',)

class EntityAdmin(admin.ModelAdmin):
    inlines = [
        TimeRageInline,
    ]

admin.site.register(Entity, EntityAdmin)

class PeriodInline(admin.TabularInline):
    model = Period
    ordering = ('start',)

class PeriodListAdmin(admin.ModelAdmin):
    inlines = [
        PeriodInline,
    ]

admin.site.register(PeriodList, PeriodListAdmin)

admin.site.register(PeriodsAndEntitiesView)