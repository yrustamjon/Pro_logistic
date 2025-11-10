from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
BOT_TOKEN = '8515822592:AAGnwNsk_fFP15_9NlCTfhyCQD_9f8W3W6Q'
CHANNEL_ID = '@aiogram2025'
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        service = data.get('service')
        message = data.get('message')
        
        # Ma’lumotni saqlash yoki email jo‘natish mumkin
        print(f"Yangi xabar: {name}, {phone}, {service}, {message}")
        # Telegram ga jo‘natish
        text = f"Yangi xabar:\nIsm: {name}\nTelefon: {phone}\nXizmat: {service}\nXabar: {message}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': CHANNEL_ID,
            'text': text,
            'parse_mode': 'HTML'
        }
        requests.post(url, data=payload)
        return JsonResponse({'message': 'Xabaringiz qabul qilindi! Tez orada siz bilan bog‘lanamiz.'})
    return render(request, 'contact.html')

