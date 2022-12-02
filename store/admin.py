from django.contrib import admin

from store.models import Category,Product,ProductImage,VariationValue

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageAdmin]
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(VariationValue)
