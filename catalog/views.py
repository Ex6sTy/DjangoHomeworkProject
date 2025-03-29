from django.shortcuts import render


def home_view(request):
    """
    Контроллер для главной страницы
    """
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

