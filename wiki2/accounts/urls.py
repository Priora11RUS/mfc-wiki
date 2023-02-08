from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
path('profile/', PasswordChangeView.as_view(template_name='wiki/profile.html'), name='password_change'),
path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]