from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Avg
from users.models import User, Vote
from cases.models import Case


# def home(request):
#     return render(request, "home.html")

def home(request):
    cases = Case.objects.filter(is_approved=1, is_completed=False)
    latest_cases = Case.objects.filter(is_approved=1, is_completed=False).order_by("-id")[:5]
    high_voted_set = (
        Vote.objects.values("case_id").annotate(total_votes=Sum('vote')).order_by("-total_votes")[:5]
    )
    featured_cases = Case.objects.filter(is_featured=1, is_completed=False)
    context = {
        "latest_cases": latest_cases,
        "high_voted_set": high_voted_set,
        "cases": cases,
        "featured_cases": featured_cases,
    }
    return render(request, "home.html", context)