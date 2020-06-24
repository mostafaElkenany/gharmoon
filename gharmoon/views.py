from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Avg
from users.models import User, Vote
from cases.models import Case


# def home(request):
#     return render(request, "home.html")

def home(request):
    cases = Case.objects.filter(is_approved=1)
    latest_cases = Case.objects.filter(is_approved=1).order_by("-id")[:5]
    high_voted_set = (
        Vote.objects.values("case_id").annotate(total_votes=Sum('vote')).order_by("-total_votes")[:5]
    )

    context = {
        "latest_cases": latest_cases,
        "high_voted_set": high_voted_set,
        "cases": cases,
    }
    return render(request, "home.html", context)