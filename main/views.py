from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/pages/about.html')


def products(request):
    return render(request, 'main/pages/products.html')


def item_product(request):
    return render(request, 'main/pages/item_product.html')


def amber(request):
    return render(request, 'main/pages/amber.html')


def light_amber(request):
    return render(request, 'main/pages/light_amber.html')


def light(request):
    return render(request, 'main/pages/light_color.html')


def extra(request):
    return render(request, 'main/pages/extra_light.html')