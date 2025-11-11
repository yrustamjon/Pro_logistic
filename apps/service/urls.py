from django.urls import path
from apps.service.views import  service_cargo,service_details0, service_details1,batafsil,batafsil0,batafsil1

urlpatterns = [
    # path('', service, name='service'),
    path('cargo/', service_cargo, name='cargo'),
    path('construction_material/', service_details0, name='construction_material'),
    path('furniture/', service_details1, name='furniture'),
    path('cargo/content_<int:pk>/', batafsil, name='batafsil'),
    path('construction_material/content_<int:pk>/', batafsil0, name='batafsil0'),
    path('furniture/content_<int:pk>/', batafsil1, name='furniture'),
]
