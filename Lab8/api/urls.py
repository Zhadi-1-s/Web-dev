from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product),
    path('categories/', views.categories_list),
    path('categories/<int:id>/',views.category),
    path('categories/<int:id>/products/',views.products_of_category)
]