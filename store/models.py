from django.db import models

from django.template.defaultfilters import slugify
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    image = models.ImageField(upload_to='category',blank=True,null=True)
    parent=models.ForeignKey("self",related_name="children", on_delete=models.CASCADE,max_length=50,blank=True,null=True)
    createddate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-createddate']
        verbose_name_plural="Categories"
class Product(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False)
    category=models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)   
    preview_desc = models.CharField(max_length=255,verbose_name="Sort decription")
    description = models.TextField(max_length=1000,verbose_name="Decription")
    images=models.ImageField(upload_to='products', blank=False,null=False)
    price = models.FloatField()
    old_price=models.FloatField(default=0.00,blank=True,null=True)
    is_stock=models.BooleanField(default=True)
    slug=models.SlugField(unique=True)
    createdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-createdate']
         
    def get_product_url(self):
        return reverse('store:product-details', kwargs={'slug':self.slug})

    def save(self, *args, **kwrags):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwrags)

class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_gellary')
    createdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)
class VariationsManager(models.Manager):
    def sizes(self):
        return super(VariationsManager,self).filter(variation='size')
    def colors(self):
        return super(VariationsManager,self).filter(variation='color')
            

VARIATIONS_TYPE =(
    ('size','size'),
    ('color','color'),
)
class VariationValue(models.Model):
    variation= models.CharField(max_length=50, choices=VARIATIONS_TYPE)
    name=models.CharField(max_length=50)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.IntegerField()
    createdate=models.DateTimeField(auto_now_add=False)

    objects=VariationsManager()

    def __str__(self):
        return self.name

class Banner(models.Model):
    product=models.ForeignKey(Product, related_name='banner', on_delete=models.CASCADE)
    baner_long_image=models.ImageField(upload_to='banner_long')
    baner_short_image=models.ImageField(upload_to='banner_short')
    baner_title=models.CharField(verbose_name="Banner Title", max_length=100)
    is_active=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name

