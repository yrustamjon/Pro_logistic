from django.shortcuts import render
from django.core.paginator import Paginator
from apps.service.models import CargoService, ConstructionMaterial, Furniture

def home(request):

    cargos = CargoService.objects.all().order_by('-created_at')
    materials = ConstructionMaterial.objects.all().order_by('-created_at')
    furnitures = Furniture.objects.all().order_by('-created_at')
    cargo_paginator = Paginator(cargos, 3)
    material_paginator = Paginator(materials, 3)
    furniture_paginator = Paginator(furnitures, 3)
    cargo_page = request.GET.get('cargo_page')
    material_page = request.GET.get('material_page')
    furniture_page = request.GET.get('furniture_page')

    context = {
        'cargos': cargo_paginator.get_page(cargo_page),
        'materials': material_paginator.get_page(material_page),
        'furnitures': furniture_paginator.get_page(furniture_page),
    }
    return render(request, 'index.html', context)
