from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Fill database with test products"

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        cat1 = Category.objects.create(name="Электроника", description="Техника")
        cat2 = Category.objects.create(name="Книги", description="Литература")

        # Создаем продукты
        Product.objects.create(name="Ноутбук", price=50000, category=cat1)
        Product.objects.create(name="Книга", price=500, category=cat2)

        self.stdout.write("Database filled successfully!")
