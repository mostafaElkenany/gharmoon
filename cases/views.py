from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
        paginator = Paginator(cases, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "cases/show_cases.html", {"cases_list":page_obj})

def search(request):
    if request.method == "GET":
        return render(request, "cases/search.html")

def search_cases(request):
    search_word = request.GET['search_word']
    cases = Case.objects.filter(name__icontains=search_word)
    print(cases)
    return render(
        request, "cases/search_results.html", {"search_results": cases},
    )
