from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def add_case(request):
    current_user = request.user
    if request.method == "POST":
        form = AddCaseForm(request.POST)
        if form.is_valid() :
            new_case = form.save(commit=False)
            new_case.owner_id = current_user.id
            new_case.save()
            
    else:
        form = AddCaseForm()
    return render(
        request, "cases/add_case.html", {"form": form},
    )