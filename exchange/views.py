from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product
from .forms import ProductNameForm

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

def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'exchange/edit.html', {'product': product})

def save(request, product_id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductNameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            product = get_object_or_404(Product, pk=product_id)
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.save()
            return HttpResponseRedirect(reverse('exchange:detail', args=(product.id,)))
        else:
            print('form.exception')
# What to do if form is not valid
#        else:
#            return HttpResponse('Boo')
# Check if we can factorize the edit and the save
#    else:
#       form = ProductNameForm()
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'exchange/edit.html', {'product': product})

@login_required
@permission_required('exchange.can_edit_product', raise_exception=True)
def product_name(request, product_id):

    product_instance = get_object_or_404(Product, pk=product_id)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = ProductNameForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            product_instance.name = form.cleaned_data['name']
            product_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('exchange:detail', kwargs={'product_id': product_id}))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ProductNameForm(initial={'name': product_instance.name})

    context = {
        'form': form,
        'product': product_instance,
    }

    return render(request, 'exchange/edit_product_name.html', context)
