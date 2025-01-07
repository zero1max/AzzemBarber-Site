from django.db import models

# Create your models here.
class Barbers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Barber Name')
    photo = models.ImageField(upload_to='images/%Y/%m/%d')
    category = models.ForeignKey("BarbersCategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class BarbersCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')

    def __str__(self):
        return self.name

class Services(models.Model):
    price_soch_olish = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Price Soch Olish')
    price_bosh_yuvish = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Price Bosh yuvish')
    price_soqol_olish = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Price SOQOL olish')
    price_for_kids = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Price for kids')
    
class Prices(models.Model):
    name = models.CharField(max_length=100, verbose_name='Prices Name')
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name
    
class Manzil(models.Model):
    city = models.CharField(max_length=100, verbose_name='City')
    address = models.CharField(max_length=100, verbose_name='Address')

    def __str__(self):
        return self.address