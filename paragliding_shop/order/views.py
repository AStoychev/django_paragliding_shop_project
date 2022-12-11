from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from paragliding_shop.equipment.models import Wings
from paragliding_shop.order.models import Product


@login_required
def cart(request):
    # products = Wings.objects.all()
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/basket.html', context)
