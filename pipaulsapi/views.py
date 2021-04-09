from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product
from .form import ProductForm

def index(request):
    latest_product_list = Product.objects.order_by('-created_at')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'pipaulsapi/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pipaulsapi/detail.html', {'product': product})

def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pipaulsapi/edit.html', {'product': product})

def save(request, product_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            product = get_object_or_404(Product, pk=product_id)
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.save()
            return HttpResponseRedirect(reverse('pipaulsapi:detail', args=(product.id,)))
        else:
            print('form.exception')
# What to do if form is not valid
#        else:
#            return HttpResponse('Boo')
# Check if we can factorize the edit and the save
#    else:
#       form = ProductForm()
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pipaulsapi/edit.html', {'product': product})


