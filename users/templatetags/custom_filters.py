from django import template
from django.db.models import Sum, Avg


register = template.Library()

@register.filter(name='check_answer')
def check_answer(is_approved):
    if is_approved == True:
        return "yes"
    else:
        return "not yet"