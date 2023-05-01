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

def product_info(request, product_slug):
    return render(request, 'store/product_info.html', {'product':get_object_or_404(models.Product, slug=product_slug)})

def category_list(request, category_slug=None):
    if not category_slug:
        return store(request)
    category_object = get_object_or_404(models.Category, slug=category_slug)
    return render(request, 'store/category_list.html', {
        'category': category_object,
        'products': models.Product.objects.filter(category=category_object)
    })