from django.shortcuts import render
from .forms import AddCaseForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Case
from django.db.models import Sum, Avg
from django.shortcuts import redirect
from users import models
from django.contrib import messages

import stripe
stripe.api_key = "sk_test_51GsEMiDFwFxU8fy1lQO5T2G4n7f5rlyfCJ4DeKRvjxqopZBDrWM1N9JEeFq7V85Ef9GM1mkfZNd5W87UG7NxBYzN00cO8PKnYC"

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

def advanced_search(request):
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

def charge(request, id):
    if request.method == "POST":
        amount = int(request.POST['amount'])
        if amount > 0:
            try:
                case = Case.objects.get(pk=id)
                amount = int(request.POST['amount'])
                user = request.user
                customer = stripe.Customer.create(
                    email=user.email,
                    source=request.POST['stripeToken'],
                )
                charge = stripe.Charge.create(
                    customer=customer,
                    amount=amount*100,
                    currency="egp",
                    description=f"Donation for case {id}",
                )
                donation = models.Donation()
                donation.user = user
                donation.amount = amount
                donation.case = case
                donation.save()
                messages.success(request, 'Thank You. We received your donation successfully')
                return redirect(request.META['HTTP_REFERER'])
            except stripe.error.CardError as e:
                messages.error(request, e.error.message )
                return redirect(request.META['HTTP_REFERER'])
            except stripe.error.RateLimitError as e:
                messages.error(request, e.error.message )
                return redirect(request.META['HTTP_REFERER'])
            except Exception as e:
                messages.error(request, "Something went wrong" )
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Invalid Amount Input")
            return redirect(request.META['HTTP_REFERER'])
