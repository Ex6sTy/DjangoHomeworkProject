from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
from blog.models import BlogPost
import sys

class Command(BaseCommand):
    """Создаёт группы с нужными правами"""
    def handle(self, *args, **kwargs):
        # ---- Модератор продуктов ----
        moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")
        product_ct = ContentType.objects.get_for_model(Product)

        # Права: кастомное право + удаление любого продукта
        can_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=product_ct)
        can_delete = Permission.objects.get(codename='delete_product', content_type=product_ct)
        moderator_group.permissions.set([can_unpublish, can_delete])

        # ---- Контент-менеджер ----
        content_manager_group, created = Group.objects.get_or_create(name="Контент-менеджер")
        # Пример: все права на BlogPost (создание, изменение, удаление, просмотр)
        blog_ct = ContentType.objects.get_for_model(BlogPost)
        perms = Permission.objects.filter(content_type=blog_ct)
        content_manager_group.permissions.set(perms)

        self.stdout.write(self.style.SUCCESS('Группы и права успешно созданы и назначены!'))


