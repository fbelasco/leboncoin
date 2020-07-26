from rest_framework.routers import DefaultRouter
from leboncoin.views import AnnonceViewSet

router = DefaultRouter()

router.register('annonces', AnnonceViewSet)
