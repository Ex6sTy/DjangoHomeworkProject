from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Создаёт группы и назначает им права"

    def handle(self, *args, **options):
        groups = {
            "Модератор продуктов": [
                "can_unpublish_product",
                "delete_product",
            ],
            "Контент-менеджер": [
                "add_blogpost",
                "change_blogpost",
                "delete_blogpost",
            ],
        }

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                app_label = "catalog" if "product" in codename else "blog"
                perm = Permission.objects.get(content_type__app_label=app_label, codename=codename)
                group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"Группа «{group_name}» настроена."))
