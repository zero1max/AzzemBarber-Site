from django.shortcuts import render
from .models import Services, Prices, Manzil, Barbers, BarbersCategory

# Create your views here.
def home(request):
    barbers = Barbers.objects.all()
    barbers_category = BarbersCategory.objects.all()
    services = Services.objects.all()
    prices = Prices.objects.all()
    manzil = Manzil.objects.all()
    context = {
        'barbers': barbers,
        'barbers_category': barbers_category,
        'services': services, 
        'prices': prices,
        'manzillar': manzil
        }
    return render(request, 'index.html', context=context)