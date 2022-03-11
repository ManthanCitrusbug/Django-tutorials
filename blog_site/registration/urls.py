from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('regi',views.registration_form),
    path('try',views.login),
    # path('',views.welcome_page),
]