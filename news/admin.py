from django.contrib import admin
from news.models import Category, Product

admin.site.register([Category])


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'picture')
