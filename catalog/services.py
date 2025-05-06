from django.core.cache import cache
from config.settings import CACHE_ENABLED
from .models import Product

def get_products_by_category(slug):
    """
    Возвращает queryset продуктов из категории slug.
    Результат кешируется на 10 минут.
    """
    cache_key = f'products_in_category_{slug}'
    products = cache.get(cache_key)
    if products is None:
        products = Product.objects.filter(category__slug=slug, status='published')
        cache.set(cache_key, products, 60 * 10)
    return products
