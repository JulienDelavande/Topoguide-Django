from django.shortcuts import render

from .models import Itineraire

def listeItineraires(request):
    ListeItineraires = Itineraire.objects.all()
    context = {"ListeItineraires" : ListeItineraires}
    return render(request, "itineraires/listeItineraires.html", context)
