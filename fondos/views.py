from fondos.models import Banco
from rest_framework import views 
from fondos.serializers import BancoSerializer
from rest_framework import generics

class BancoView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
