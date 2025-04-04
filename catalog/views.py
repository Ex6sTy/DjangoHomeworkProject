from django.shortcuts import render, get_object_or_404
from .models import Product


def home_view(request):
    """
    Контроллер для главной страницы
    """
    latest_products = Product.objects.order_by('-created_at')[:5]
    print("Последние 5 продуктов:", list(latest_products))
    return render(request, 'catalog/home.html')


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