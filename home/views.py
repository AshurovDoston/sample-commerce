from django.shortcuts import render
from products.models import Product, Category


def home_view(request):
    categories = Category.objects.filter(is_active=True)[:6]
    featured_products = Product.objects.filter(
        is_available=True
    ).select_related("category").prefetch_related("rasmlar")[:8]

    context = {
        "categories": categories,
        "featured_products": featured_products,
    }
    return render(request, "home.html", context)