from rest_framework.viewsets import ModelViewSet
from .serializers import AnnonceSerializer
from .models import Annonce

class AnnonceViewSet(ModelViewSet):
    serializer_class = AnnonceSerializer
    queryset = Annonce.objects.all()
