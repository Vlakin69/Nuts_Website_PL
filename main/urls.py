from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('poducts', views.products),
    path('item-product', views.item_product),
]
