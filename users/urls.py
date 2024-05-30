from django.urls import path
from django.views.generic import TemplateView

from users import views

app_name = 'users'

urlpatterns = [
    path('register/',views.UserRegister.as_view() ,name='register'),
    path('success', TemplateView.as_view(template_name='users/success_register.html'), name='success')
]

