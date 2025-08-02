from django.contrib import admin
from .models import JewelryItm, JewelryImage

class JewelryImageInline(admin.TabularInline):
    model = JewelryImage
    extra = 1

@admin.register(JewelryItm)
class JewelryItmAdmin(admin.ModelAdmin):
    list_display = ('name','price','created_at')
    inlines = [JewelryImageInline]



# Register your models here.
