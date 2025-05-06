from django.core.cache import cache
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (HomeView,
                    ContactView,
                    ProductDetailView,
                    ProductCreateView,
                    ProductDeleteView,
                    ProductUpdateView,
                    ProductUnpublishView,
                    CategoryProductListView,
                    ProductListView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('category/<slug:slug>/', CategoryProductListView.as_view(), name='category_products'),
]
