from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Product
from .forms import ProductForm


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 10


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        product.views += 1
        product.save()
        return product


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('home')  # Перенаправление на главную после добавления товара
#