from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    This is a basic API view that returns a random product from the database.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response(data)
