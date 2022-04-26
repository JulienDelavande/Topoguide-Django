from distutils.log import Log
from django.shortcuts import get_object_or_404, redirect, render

from .models import Itineraire, Sortie
from .forms import SortieForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def listeItineraires(request):
    """
    Renvoie la liste de tous les itinéraires disponibles (rentrés un admin)
    Possibilité :
    -d'acceder aux sorties correspondant à l'itinéraire en cliquant sur l'itinéraire voulu
    -de se connecter/déconnecter
    Si l'utilisateur est connecté ajouter des sorties
    """
    ListeItineraires = Itineraire.objects.all()
    context = {"ListeItineraires" : ListeItineraires, 'utilisateur':request.user}
    return render(request, "itineraires/listeItineraires.html", context)


def listeSorties(request, itineraire_id):
    """
    Renvoie la liste des sorties correspondant à un itinéraire
    Possibilité :
    -de consulter de le détail d'une sortie
    -de modifier une de ses sorties
    -de se connecter/déconnecter
    -de revenir à la liste des itinéraires (menu pricipal)
    Si l'utilisateur est connecté, il peut modifier ses sorties et ajouter des sorties
    """
    itineraireSortie = get_object_or_404(Itineraire, pk = itineraire_id)
    ListeSorties = Sortie.objects.filter(itineraire = itineraireSortie)
    context = {"itineraire":itineraireSortie, "ListeSorties":ListeSorties}
    return render(request, "itineraires/listeSorties.html", context)


def sortieDetails(request, sortie_id):
    """
    Détail d'une sortie
    Possibilité :
    -de se connecter/déconnecter
    -de revenir à la liste des itinéraires (menu pricipal)
    """
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    context = {"sortie":sortie}
    return render(request, "itineraires/sortieDetails.html", context)


def ajouterSortie(request):
    """
    Formulaire pour ajouter une sortie
    Possibilité :
    -d'enregistrer sa sortie avec les informations saisies
    -de se connecter/déconnecter
    -de revenir à la liste des itinéraires (menu pricipal)
    """
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.utilisateur = request.user
            sortie.save()
            context = {'sortie':sortie}
            return render(request, 'itineraires/sortieDetails.html', context)

    else:
        
        form = SortieForm()
    context = {'form':form, 'sortie_id':0}
    return render(request, 'itineraires/ajouterModifSortie.html', context)
    
    
@login_required(redirect_field_name='login')
def ajouterModifSortie(request,sortie_id):
    """
    Formulaire pour modifier une sortie
    Possibilité :
    -d'enregistrer sa sortie modifiée avec les informations saisies
    -de se connecter/déconnecter
    -de revenir à la liste des itinéraires (menu pricipal)
    """
    if sortie_id == 0:
        return ajouterSortie(request)
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    if sortie.utilisateur != request.user:
        return redirect("login")
    if request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.utilisateur = request.user
            sortie.save()
            context = {'sortie':sortie}
            return render(request, 'itineraires/sortieDetails.html', context)

    else:
        form = SortieForm(instance=sortie)
    context = {'form':form, 'sortie_id':sortie_id, 'sortie':sortie}
    return render(request, 'itineraires/ajouterModifSortie.html', context)
