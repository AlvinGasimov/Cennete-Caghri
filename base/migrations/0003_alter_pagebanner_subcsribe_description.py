# Generated by Django 5.1.4 on 2025-01-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pagebanner_subcsribe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebanner',
            name='subcsribe_description',
            field=models.TextField(verbose_name='Abone Ol Banner Kısa Açıklaması'),
        ),
    ]
