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

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ProductForm(request.POST, request.FILES)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            product.name=form.cleaned_data['name']
            product.description=form.cleaned_data['description']
            product.price=form.cleaned_data['price']
            product.image=form.cleaned_data['image']
            product.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('exchange:product-detail', args=[product.id]) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price':product.price,
            'image':product.image,
        })

    context = {
        'form': form,
    }

    return render(request, 'exchange/product_form.html', context)


def product_create(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ProductForm(request.POST, request.FILES)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            product = Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                image=form.cleaned_data['image'],
            )
            product.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('exchange:product-detail', args=[product.id]) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'exchange/product_form.html', context)


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('exchange:index')

