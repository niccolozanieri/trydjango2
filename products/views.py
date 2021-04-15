from django.shortcuts import render
from .models import Product
from .forms import CreateProductForm

# Create your views here.

def products_list_view(request):
    products = Product.objects.all()
    context = {
        'products_list': products
    }
    return render(request, "products/products_list.html", context)

def products_create_view(request):
    form = CreateProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateProductForm()
    context = {
        "form": form
    }
    return render(request, "products/products_create.html", context)