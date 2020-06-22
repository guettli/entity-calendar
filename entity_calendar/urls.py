import entity_calendar.views
from django.urls import path

urlpatterns = [
    path('', entity_calendar.views.homepage, name='homepage'),
    path('period_and_entity_view/<int:pk>/', entity_calendar.views.period_and_entity_view, name='period_and_entity_view'),
    ]

