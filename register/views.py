from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from users.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Account.'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Registerd successfully, Please confirm your email address to complete the registration')
            return redirect("login")
            # return HttpResponse('Please confirm your email address to complete the registration')
            # form.save()
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=password)
            # login(request, user)
            # return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form":form})


def activate(request, uidb64, token,backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.signup_confirmation = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Thank you for your email confirmation.')
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')
