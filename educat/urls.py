from django.urls import path, re_path
from . import views



urlpatterns = [

	path('', views.index),

	path('categories/', views.category, name="categories"),

	path('search/<str:query>/', views.search, name="search"),

    path('module/<int:id>/', views.moduledetails, name="moduledetails"),





]