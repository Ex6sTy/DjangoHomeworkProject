from django.urls import path
from .views import home_view, contacts_view, product_detail, add_product

urlpatterns = [
    path('', home_view, name='home'),
    path('contacts/', contacts_view, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
]
