from django.contrib import admin
from app1.models import Category,SubCategory,Product,Color,Size,Brand,ProductImage,ProductDetails,Cart,Order

# Inline form
class ImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1
    
class ProductDetailsAdmin(admin.StackedInline):
    model = ProductDetails
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin , ProductDetailsAdmin]
    
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    
# Admin site registration
admin.site.register(Product , ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(Cart,CartAdmin)