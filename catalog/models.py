from django.db import models

class JewelryItm(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JewelryImage(models.Model):
    item = models.ForeignKey(JewelryItm, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='jewelry_images/')

    def __str__(self):
        return f"Image for {self.item.name}"
# Create your models here.
