from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required
from .models import Case
from django.db.models import Sum, Avg
from django.shortcuts import redirect


# @login_required(login_url='/accounts/login/')
def add_case(request):
    if request.method == "POST":
        form = AddCaseForm(request.POST)
        if form.is_valid() :
            new_case = form.save(commit=False)
            new_case.owner_id = 1
            new_case.save()
            
    else:
        form = AddCaseForm()
    return render(
        request, "cases/add_case.html", {"form": form},
    )


def view_case(request, id):
    case = Case.objects.get(pk=id)
    case_donations = case.donation_set.aggregate(total_amount=Sum('amount'))
    case_votes = case.vote_set.aggregate(total_votes=Sum('vote'))
    context = {
                "case": case,
                "is_reported": request.user.case_reports.filter(id=case.id).exists(),
                "case_donations": case_donations,
                "votes":case_votes['votes'],
                # "donation_form": DonateForm()
            }
        
    return render(request, "cases/view.html", context)


def report_case(request, id):
    if request.method == "POST":
        case = Case.objects.filter(id=id)
        if case.exists():
            project = project.first()
            if not request.user.project_reports.filter(id=project.id).exists():
                request.user.project_reports.add(project)
            return redirect("view_project", id=project.id)
    return redirect("home")