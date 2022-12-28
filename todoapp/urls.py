from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('home', views.homePage, name='home'),
    path('login', views.loginPage, name='login'),
    path('about', views.aboutPage, name='about'),
    path('contact', views.contactPage, name='contact'),
    path('todolist', views.todoPage, name='todolist'),
]
