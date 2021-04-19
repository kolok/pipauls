from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductNameForm, ProductForm

def index(request):
    return HttpResponseRedirect(reverse('exchange:product-list'))

def product_list(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    latest_product_list = Product.objects.order_by('-created_at')[:5]
    context = {
        'latest_product_list': latest_product_list,
        'num_visits': request.session['num_visits'],
    }
    return render(request, 'exchange/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'exchange/detail.html', {'product': product})

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('exchange:index')

