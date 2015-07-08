from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .models import Product

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'cleanly/index.html'

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'cleanly/detail.html', {'product': product})

@login_required(login_url='/')
def buy(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    # save history
    product = request.user.history_set.filter(product_id=p.id)
    if product:
        product[0].quantity += 1
        product[0].save()
    else:
        h = request.user.history_set.create(product_id=p.id, product_header=p.header, product_description=p.decription, product_price=p.price)
    return HttpResponseRedirect(reverse('cleanly:thank_you', args=(p.id,)))

@login_required(login_url='/')
def thank_you(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    return render(request, 'cleanly/thank_you.html', {'product': p})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)

    return HttpResponseRedirect(reverse('cleanly:index'))

@login_required(login_url='/')
def my_account(request):
    history_products = request.user.history_set.all()
    return render(request, 'cleanly/my_account.html', {'products': history_products})
