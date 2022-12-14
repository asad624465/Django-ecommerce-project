from multiprocessing import context
from django.shortcuts import render

from django.views.generic import ListView,DetailView
#load model for showing product in home page
from store.models import Product,Category,ProductImage,Banner

class ProductsList(ListView):
    model= Product
    template_name='frontend/index.html'
    context_object_name='products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["banners"] = Banner.objects.filter(is_active=True).order_by('-id')[0:3]
        return context
    
class productDetails(DetailView):
    model=Product
    template_name='frontend/product_details.html'
    context_object_name= 'item'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object.id)
        return context

#def productDetails(req, id):
#    item = Product.objects.get(id=id)
#    photos=ProductImage.objects.filter(product=item).order_by('-createdate')
#    context={'item':item,'photos':photos}
#    return render(req,'frontend/product_details.html',context)
