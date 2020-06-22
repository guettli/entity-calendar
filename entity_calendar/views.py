from django.shortcuts import render

# Create your views here.
from django.utils.html import format_html, format_html_join
from entity_calendar.models import PeriodsAndEntitiesView
from entity_calendar.utils import join


def homepage(request):
    rows = []
    for view in PeriodsAndEntitiesView.objects.all().order_by('name'):
        rows.append(format_html('<tr><th><a href="{}">{}</a></th></tr>',
                                view.get_absolute_url(), view.name))
    content = format_html('<table>{}</table', join(rows))
    return render(request, 'entity_calendar/base.html', context=dict(content=content))

def period_and_entity_view(request, pk):
    view = PeriodsAndEntitiesView.objects.get(pk=pk)
    rows=[]

    cells = []
    for period in view.period_list.periods.order_by('start'):
        delta = period.end - period.start
        cells.append(format_html('<th class="is_first" colspan="{}">{}</th>', delta.days+1, period.name))
    rows.append(format_html('<tr><td></td>{}</tr>', join(cells)))

    cells = []
    for day, is_first in view.days():
        cells.append(format_html('<td class="day_heading {}">{}<br>{}</td>',
                                 'is_first' if is_first else '',
                                 day.month, day.day))
    rows.append(format_html('<tr><td>Month<br>Day</td>{}</tr>', join(cells)))


    for entity in view.entities.order_by('name'):
        cells = []
        for day, is_first in view.days():
            char = ''
            if entity.day_is_in_one_range(day):
                char = 'X'
            cells.append(format_html('<td class="day {} x_cell">{}</td>',
                                     'is_first' if is_first else '',
                                     char))
        rows.append(format_html('<tr class="entity_row"><th class="entity_name"><a href="{}">{}</a></th>{}</tr>',
                                entity.get_absolute_url(),
                                entity.name, join(cells)))
    content = format_html('''<h1>{}</h1>
                          <table>{}</table>''', view.name, join(rows, '\n'))
    return render(request, 'entity_calendar/base.html',
                  context=dict(content=content,
                               title=view.name,
                               ))
