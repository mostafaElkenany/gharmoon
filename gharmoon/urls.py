from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from .views import home
from register.views import register, activate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cases/', include('cases.urls')),
    path('profile/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',register,name='register'),
    path('accounts/',include('allauth.urls')),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('', home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)