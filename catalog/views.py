from rest_framework import viewsets
from .models import JewelryItm
from .serializers import JewelryItemSerializer

class JewelryItemViewSet(viewsets.ModelViewSet):
    queryset = JewelryItm.objects.all()
    serializer_class = JewelryItemSerializer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cors_test_view(request):
    return JsonResponse({"message": "CORS test passed!"})

    


# Create your views here.
