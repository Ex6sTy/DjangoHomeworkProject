from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Category
from .services import get_products_by_category


class HomeView(ListView):
    model = Product
    ordering = ['-created_at']
    paginate_by = 10
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        success = False
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            success = True
        return self.render_to_response({'success': success})

@method_decorator(cache_page(60 * 15), name='dispatch')  # кеш 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# ---- Только авторизованные пользователи ----

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # <--- вот это важно!
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("Редактировать продукт может только владелец.")
        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        is_moderator = user.groups.filter(name='Модератор продуктов').exists()
        if obj.owner != user and not is_moderator:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("Удалять продукт может только владелец или модератор.")
        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        # Только если пользователь — модератор с этим правом
        if request.user.has_perm('catalog.can_unpublish_product'):
            product.status = 'unpublished'
            product.save()
            messages.success(request, 'Продукт снят с публикации.')
        else:
            messages.error(request, 'У вас нет прав для снятия продукта с публикации.')
        return redirect('product_detail', pk=pk)

class CategoryProductListView(ListView):
    template_name = 'catalog/category_products.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return get_products_by_category(self.category.slug)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = self.category
        return ctx