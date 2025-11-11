from django.shortcuts import render
from django.core.paginator import Paginator
from apps.common.models import Service, BannerImage
from apps.service.models import CargoService, ConstructionMaterial, Furniture

# def service(request):
#     services = Service.objects.all().order_by('created_at')
#     print(services)
#     return render(request, 'service.html', {'services': services})

def service_cargo(request):
    cargo=CargoService.objects.all().order_by('-created_at')
    services=Service.objects.get(name='Kargo')
    if services:
        images=BannerImage.objects.filter(service=services)
    print(len(images))
    paginator = Paginator(cargo,6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services_detail.html', {'page_obj': page_obj,'services':services,'images':images})

def service_details0(request):
    material=ConstructionMaterial.objects.all().order_by('-created_at')
    services=Service.objects.get(name='Stroy materyallar')
    if services:
        images=BannerImage.objects.filter(service=services)
    print(len(images))
    paginator = Paginator(material,6)  # 1 sahifada 6 ta karta chiqadi
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services_detail0.html',{'page_obj': page_obj,'services':services,'images':images})

def service_details1(request):
    furniture=Furniture.objects.all().order_by('-created_at')
    services=Service.objects.get(name='Stol-Stul')
    if services:
        images=BannerImage.objects.filter(service=services)
    print(len(images))
    paginator = Paginator(furniture,6)  # 1 sahifada 6 ta karta chiqadi
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'services_detail1.html',{'page_obj': page_obj,'services':services,'images':images})

def batafsil(request,pk):
    service=CargoService.objects.get(pk=pk)
    if service:
        images=service.images.all()
        
    return render(request, 'batafsil.html',{'service':service,'images':images})

def batafsil0(request,pk):
    service=ConstructionMaterial.objects.get(pk=pk)
    if service:
        images=service.images.all()
        
    return render(request, 'batafsil0.html',{'service':service,'images':images})

def batafsil1(request,pk):
    service=Furniture.objects.get(pk=pk)
    if service:
        images=service.images.all()
        
    return render(request, 'batafsil1.html',{'service':service,'images':images})