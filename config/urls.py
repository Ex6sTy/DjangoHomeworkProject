from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Все пути из приложения catalog будут доступны по корню сайта
    path('', include('catalog.urls')),
]
