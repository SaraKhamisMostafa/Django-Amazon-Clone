from django.contrib import admin
from .models import Product, ProductImages , Brand, Review
# Register your models here.


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra=3

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','brand','quantity','price']
    list_filter=['brand','quantity','price','tags']
    search_fields=['name','subtitle','description']
    inlines=(ProductImagesInline,)


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)