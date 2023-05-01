from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('product/<slug:product_slug>', views.product_info, name='product_info'), # individual product
    path('search/<slug:category_slug>', views.category_list, name='category_list') # individual category products
]
