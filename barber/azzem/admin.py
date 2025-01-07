from django.contrib import admin
from .models import Services, Prices, Manzil, Barbers, BarbersCategory
from django.utils.html import format_html

# Register your models here.
class BarbersAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_tag')

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'

class BarbersCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('price_soch_olish', 'price_bosh_yuvish', 'price_soqol_olish', 'price_for_kids')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class ManzilAdmin(admin.ModelAdmin):
    list_display = ('city', 'address')

admin.site.register(Barbers, BarbersAdmin)
admin.site.register(BarbersCategory, BarbersCategoryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Prices, PriceAdmin)
admin.site.register(Manzil, ManzilAdmin)