from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

def index(request):
    latest_product_list = Product.objects.order_by('-created_at')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'pipaulsapi/index.html', context)

def detail(request, product_id):
    return HttpResponse("You're looking at question %s." % product_id)
