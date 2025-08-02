from rest_framework import serializers
from .models import JewelryItm, JewelryImage

class JewelryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JewelryImage
        fields = ['id', 'image']


class JewelryItemSerializer(serializers.ModelSerializer):
    images = JewelryImageSerializer(many=True, read_only=True)

    class Meta:
        model = JewelryItm
        fields = ['id','name','description','price','images']