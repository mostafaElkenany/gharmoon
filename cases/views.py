from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Case
from django.db.models import Sum, Avg
from django.shortcuts import redirect


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

def view_case(request, id):
    case = Case.objects.get(pk=id)
    case_donations = case.donation_set.aggregate(total_amount=Sum('amount'))
    case_votes = case.vote_set.aggregate(total_votes=Sum('vote'))
    context = {
                "case": case,
                "is_reported": request.user.case_reports.filter(id=case.id).exists(),
                "case_donations": case_donations,
                "votes":case_votes,
                # "donation_form": DonateForm()
            }
        
    return render(request, "cases/view.html", context)

def report_case(request, id):
    if request.method == "POST":
        case = Case.objects.filter(id=id)
        if case.exists():
            case = case.first()
            if not request.user.case_reports.filter(id=case.id).exists():
                request.user.case_reports.add(case)
            return redirect("view_case", id=case.id)
    return redirect("home")
