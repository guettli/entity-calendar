from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe


def join(args, sep=''):
    return mark_safe(sep.join([conditional_escape(item) for item in args]))