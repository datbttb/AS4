from os import name

from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import register, my_account, order_details, order_info, register1
from ecomstore import settings


urlpatterns = [
    path('register/', register, {'template_name': 'registration/register.html'}, name='register'),
    path('my_account/', my_account, {'template_name': 'registration/my_account.html'}, name='my_account'),
    path('order_details/<slug:order_id>/', order_details, {'template_name': 'registration/order_details.html'},
         name='order_details'),
    path('order_info/', order_info, {'template_name': 'registration/order_info.html'}, name='order_info'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register1/', register1, name="register1"),
]
