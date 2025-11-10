from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(max_length=255,null=True)
    bid_des=models.TextField(max_length=255,null=True)
    image = models.ImageField(upload_to='service_images/',null=True)
    link=models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BannerImage(models.Model):
    service=models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='cargo_images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CargoImage {self.id}"
