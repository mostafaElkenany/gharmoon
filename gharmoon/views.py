from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum, Avg
from users.models import User, Vote
from cases.models import Case
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required


from .forms import ContactForm


def home(request):
    cases = Case.objects.filter(is_approved=1, is_completed=False)
    latest_cases = Case.objects.filter(is_approved=1, is_completed=False).order_by("-id")[:5]
    high_voted_set = (
        Vote.objects.values("case_id").annotate(total_votes=Sum('vote')).order_by("-total_votes")[:5]
    )
    featured_cases = Case.objects.filter(is_featured=1, is_completed=False).order_by("-featuring_date")[:5]
    context = {
        "latest_cases": latest_cases,
        "high_voted_set": high_voted_set,
        "cases": cases,
        "featured_cases": featured_cases,
    }
    return render(request, "home.html", context)

@login_required(login_url='/accounts/login/')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            comment = form.cleaned_data.get('comment')
            body = email + ", sent the following message:\n\n" + strip_tags(comment)
            send_mail(subject, body,'gharmoon.project@gmail.com', ['gharmoon.project@gmail.com'])
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})

def about(request):
    return render(request, "about.html")