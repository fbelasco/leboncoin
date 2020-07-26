# todo/admin.py

from django.contrib import admin
from .models import Annonce

# On spéecifie ce que l'on affiche d'une annonce : ici le titre et sa catégorie
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre','categorie')

# Register your models here.
admin.site.register(Annonce, AnnonceAdmin)
