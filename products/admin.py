from django.contrib import admin
from .models import Category, Units, Product, ProductVariant, ProductImage

admin.site.register(Category)
admin.site.register(Units)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)