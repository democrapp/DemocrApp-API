from django.urls import path, include
from django.contrib.auth import views as auth_views
from democrapp_api.settings import CLIENT_ID, CLIENT_SECRET, MANAGER_URL
from . import views

oauth_context = {
    'CLIENT_ID': CLIENT_ID,
    'CLIENT_SECRET': CLIENT_SECRET,
    'MANAGER_URL': MANAGER_URL,
}

urlpatterns = [
    path('accounts/login', auth_views.LoginView.as_view(extra_context=oauth_context)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('authorized', views.authorized)
]
