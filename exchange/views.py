from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product
from .forms import ProductNameForm, ProductForm

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    latest_product_list = Product.objects.order_by('-created_at')[:5]
    context = {
        'latest_product_list': latest_product_list,
        'num_visits': request.session['num_visits'],
    }
    return render(request, 'exchange/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'exchange/detail.html', {'product': product})

@login_required
@permission_required('exchange.can_edit_product', raise_exception=True)
def edit(request, product_id):
    product_instance = get_object_or_404(Product, pk=product_id)
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
            return HttpResponseRedirect(reverse('exchange:detail', args=(product.id,)))
    else:
        form = ProductForm(initial={
            'name': product_instance.name,
            'description': product_instance.description,
            'price': product_instance.price,
        })

    context = {
        'form': form,
        'product': product_instance,
    }
    return render(request, 'exchange/edit.html', context)
