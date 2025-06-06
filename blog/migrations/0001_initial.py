# Generated by Django 5.1.7 on 2025-04-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_previews/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Блоговая запись',
                'verbose_name_plural': 'Блоговые записи',
                'db_table': 'blog_post',
            },
        ),
    ]
