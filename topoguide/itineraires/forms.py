from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):
    """
    Formulaire pour la saisie d'une sortie par un utilsateur connecté
    """
    class Meta:
        model = Sortie
        fields = ['itineraire', 'date_sortie', 'duree_reelle', 'difficulte_estimee', 'nombre_participant', 'experience_groupe', 'meteo' ]