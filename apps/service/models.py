# apps/products/models.py

from django.db import models

# 1️⃣ Kafe Stol-Stullar
class Furniture(models.Model):
    name = models.CharField(max_length=200)
    ban_image=models.ImageField(upload_to='furniture/', null=True, blank=True)
    description = models.TextField()
    big_description = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # Video link
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Furniture uchun bir nechta rasm
class FurnitureImage(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='furniture/multi/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.furniture.name} Image"

# 2️⃣ Qurilish Materiallari
class ConstructionMaterial(models.Model):
    name = models.CharField(max_length=200)
    ban_image=models.ImageField(upload_to='construction/', null=True, blank=True)
    description = models.TextField()
    big_description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ConstructionMaterialImage(models.Model):
    material = models.ForeignKey(ConstructionMaterial, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='construction/multi/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material.name} Image"

# 3️⃣ Cargo Xizmatlari
class CargoService(models.Model):
    name = models.CharField(max_length=200)
    ban_image=models.ImageField(upload_to='cargo/', null=True, blank=True)
    description = models.TextField()
    big_description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CargoServiceImage(models.Model):
    cargo = models.ForeignKey(CargoService, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cargo/multi/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cargo.name} Image"
