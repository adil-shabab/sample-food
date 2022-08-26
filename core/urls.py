from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('breakfast', views.breakfast, name='breakfast'),
    path('lunch', views.lunch, name='lunch'),
    path('dinner', views.dinner, name='dinner'),
    path('order/<str:category>', views.order, name='order'),
    path('accounts/login', views.login, name='login'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logoutUser, name='logout'),
]