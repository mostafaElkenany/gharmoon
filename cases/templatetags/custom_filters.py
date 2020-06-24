from django import template
from django.db.models import Sum, Avg


register = template.Library()

@register.filter(name='check_answer')
def check_answer(is_approved):
    if is_approved == True:
        return "yes"
    else:
        return "not yet"

@register.filter(name='total_votes')
def total_votes(case):
    case_votes = case.vote_set.aggregate(total_votes=Sum('vote'))
    return int(case_votes['total_votes'] or 0)


@register.filter(name='case_donations')
def case_donations(case):
    return case.donation_set.aggregate(total_amount=Sum('amount'))['total_amount'] or 0