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
    

