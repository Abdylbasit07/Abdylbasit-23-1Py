from django.shortcuts import render
from posts.models import Product

# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'products/products.html', context={
            'products': products
        })