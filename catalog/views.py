from rest_framework import viewsets
from .models import JewelryItm
from .serializers import JewelryItemSerializer

class JewelryItemViewSet(viewsets.ModelViewSet):
    queryset = JewelryItm.objects.all()
    serializer_class = JewelryItemSerializer

    


# Create your views here.
