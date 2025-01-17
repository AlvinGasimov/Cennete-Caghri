# Generated by Django 5.1.4 on 2025-01-17 16:06

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Makale Kategori Adı')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Makale Kategori Oluşturulma Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Makale Kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Makale Başlığı')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Makale Açıklaması')),
                ('author', models.CharField(max_length=200, verbose_name='Makale Yazarı')),
                ('image', models.ImageField(upload_to='article_images/', verbose_name='Makale Resmi')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Makale Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Makale Güncellenme Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='article.articlecategory', verbose_name='Makale Kategorisi')),
            ],
            options={
                'verbose_name_plural': 'Makaleler',
            },
        ),
    ]
