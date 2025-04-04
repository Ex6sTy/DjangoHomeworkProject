from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


def home_view(request):
    """
    Контроллер для главной страницы
    """
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/home.html', {'page_obj': page_obj})



def contacts_view(request):
    """
    Контроллер для страницы контактов и обработки формы
    """
    success = False

    if request.method == 'POST':
        # Считываем данные формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        success = True

    return render(request, 'catalog/contacts.html', {'success': success})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу после добавления товара
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
