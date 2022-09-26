from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('poducts', views.products),
    path('item-product', views.item_product),
    path('amber', views.amber),
    path('light-amber', views.light_amber),
    path('light', views.light),
    path('extra', views.extra),

]
