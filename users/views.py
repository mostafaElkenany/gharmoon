from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import UserForm, ConfirmPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User



@login_required(login_url='/accounts/login/')
def show_profile(request):
    current_user = request.user
    context = {"user": current_user}
    return render(request, "users/user_profile.html", context)

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.save()
            return redirect("profile")
    else:
        form = UserForm(instance=current_user)

    return render(request, "users/edit_profile.html", {"form": form})

@login_required(login_url='/accounts/login/')
def change_password(request):
    current_user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(current_user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(current_user)
    return render(request, "users/change_password.html", {"form": form})

@login_required(login_url='/accounts/login/')
def delete_account(request):
    current_user = request.user
    password_form = ConfirmPasswordForm(request.POST, instance=current_user)
    if request.method == "POST":
        if password_form.is_valid():
            current_user.delete()
            return redirect("home")
    else:
        password_form = ConfirmPasswordForm(instance=current_user)
    return render(request, "users/delete_account.html", {"form": password_form})

@login_required(login_url='/accounts/login/')
def get_cases(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    cases = user.case_set.all()
    context = {
        "cases": cases,
    }
    return render(request, "users/user_cases.html", context)



@login_required(login_url='/accounts/login/')
def get_donations(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    donations = user.case_donations.distinct()
    context = {
        "donations": donations,
    }
    return render(request, "users/user_donations.html", context)
