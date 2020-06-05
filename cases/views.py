from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required
from .models import Case

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

def show_cases(request):
    if request.method == "GET":
        cases = Case.objects.all()
        return render(request, "cases/show_cases.html", {"cases_list":cases})