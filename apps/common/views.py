from django.shortcuts import render
from apps.common.models import Service

def home(request):
    services = Service.objects.all().order_by('created_at')
    context = {
        'services': services,
    }
    return render(request, 'index.html', context)
