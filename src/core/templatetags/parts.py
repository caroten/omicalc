import ipdb
from django import template
from django.template.loader import get_template
from ..models import Publication, Issue
from ..views import get_issue_filter_params
from ..utils import State, Period
from ..consts import *
from ..forms import LineForm

register = template.Library()

@register.inclusion_tag('publication-sidebar.html')
def pubs(active=None):
    pubs = Publication.objects.all()
    return { 'pubs': pubs,
             'active': active, }

@register.inclusion_tag('issues-table.html')
def issues0(active=None):
    param = {'publication': active} if active else {}
    issues = Issue.objects.filter(**param).order_by('-date')
    return { 'issues': issues }

@register.inclusion_tag('issues-table.html')
def issues(qs):
    return { 'issues': qs }

@register.inclusion_tag('nav-state.html')
def nav_state1(state=None):
    if state == {}: state = State()
    states = [{'value': v, 'text': t} for v,t in Issue.STATES_NAME]
    state = [i for i in states if i['value']==state.name][0] if [i for i in states if i['value']==state.name] else State.default()
    return { 'states': states, 'state': state }

@register.inclusion_tag('nav-state.html')
def nav_state(state=None):
    states = [{'value': v, 'text': t} for v, t in ISSUE_STATES]
    if not state:
        state = State()
    state = [i for i in states if i['value']==state.name][0] if [i for i in states if i['value']==state.name] else State.default()
    return { 'states': states, 'state': state }

@register.inclusion_tag('nav-period.html')
def nav_period(period=None):
    periods = [Period(i, 'month')
               for i in Issue.objects.datetimes('date','month')]
    period = period or Period.default()
    return { 'periods': periods, 'period': period }

@register.inclusion_tag('line-table.html')
def line_table(detail):
    lines = detail.lines.all()
    return {
        'forms': [
            LineForm({k: getattr(line, k) for k in LineForm.Meta.fields})
            for line in lines
        ],
    }

@register.inclusion_tag('args-table.html')
def args_table(detail):
    return {}
