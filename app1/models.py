from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# #created models
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', limit_choices_to={'name__in': Category.objects.values('name')})

    def __str__(self):
        return self.name
    
# # abstract class it use avoid repetation
    
class ClothsProperty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
        
# # inherited class of abstract class

class Brand(ClothsProperty):
    pass

class Size(ClothsProperty):
    pass

class Color(ClothsProperty):
    pass

class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Men'),
        ('W', 'Women'),
        ('B', 'Both'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, limit_choices_to={'name__in': SubCategory.objects.values('name')})
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, limit_choices_to={'name__in': Brand.objects.values('name')})
    size = models.ForeignKey(Size, on_delete=models.CASCADE, limit_choices_to={'name__in': Size.objects.values('name')})
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def category(self):
    #     return self.subcategory.category

    # def __str__(self):
    #     return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/')
    image3 = models.ImageField(upload_to='product_images/')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, limit_choices_to={'name__in': Color.objects.values('name')})

    def __str__(self):
        return f"{self.product.name} - {self.color.name} Image"
    

class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details')
    main = models.CharField(max_length = 50)
    sub = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.product.name} Details"

class Cart(models.Model):
    uid = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    pColor = models.CharField(max_length = 100,default="null")
    size = models.CharField(max_length = 10,default="null")
    qty = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=12, decimal_places=2,default = 1.2)
    
class Order(models.Model):
    uid = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    pColor = models.CharField(max_length = 100,default="null")
    size = models.CharField(max_length = 10,default="null")
    qty = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    price = models.DecimalField(max_digits=12, decimal_places=2,default = 1.2)