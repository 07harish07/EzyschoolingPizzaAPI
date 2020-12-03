from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PizzaCreateView, name='home'),
    path('pizza/list', views.PizzaListView, name='home'),
    path('pizza/update/<str:id>', views.PizzaUpdateView, name='update'),
    path('pizza/delete/<str:id>', views.PizzaDeleteView, name='delete'),
]