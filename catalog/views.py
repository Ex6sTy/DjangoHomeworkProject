from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product

def home_view(request):
    """
    Контроллер для главной страницы
    """
    # Получаем все продукты из базы данных
    products = Product.objects.all()

    # Пагинация: показываем по 10 товаров на странице
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