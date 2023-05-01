from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.


def store(request):
    return render(request, 'store/store.html', {'all_products': models.Product.objects.all()})


def categories(request):
    all_categories = models.Category.objects.all()
    return {
        'all_categories': all_categories
    }

def product_info(request, slug):
    return render(request, 'store/product_info.html', {'product':get_object_or_404(models.Product, slug=slug)})