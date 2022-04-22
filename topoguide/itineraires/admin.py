from django.contrib import admin


from .models import Itineraire, Sortie

# Enregistrement des models de l'app itineraire
admin.site.register(Itineraire)
admin.site.register(Sortie)

