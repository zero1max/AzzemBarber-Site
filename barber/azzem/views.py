from django.shortcuts import render
from .models import Services, Prices, Manzil, Barbers, BarbersCategory
from services.bot import send_msg

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

def process_booking(request):
    if request.method == 'POST':
        # Foydalanuvchi tomonidan yuborilgan ma'lumotlarni olish
        name = request.POST.get('bb-name')
        phone = request.POST.get('bb-phone')
        booking_time = request.POST.get('bb-time')
        booking_date = request.POST.get('bb-date')
        message = request.POST.get('bb-message', 'Fikr-mulohaza mavjud emas')  # ixtiyoriy

        # Telegramga yuboriladigan xabarni formatlash
        telegram_message = (f"📝 Yangi bron ma'lumotlari:\n\n👤 Ismi: {name}\n📞 Telefon: {phone}\n📅 Kun: {booking_date}\n⏰ Vaqt: {booking_time}\n💬 Fikr-mulohaza: {message}\n"
        )

        # Telegram botga yuborish
        send_msg(telegram_message)  # send_msg funksiyasini chaqiramiz

        # Foydalanuvchiga javob
        return render(request, 'booking_success.html', {'name': name})

    # Agar GET so'rov bo'lsa, bronlash formasini qaytaramiz
    return render(request, 'booking_form.html')