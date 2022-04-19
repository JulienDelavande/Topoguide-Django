from django.db import models
from django.contrib.auth.models import User


class Itineraire(models.Model):
    titre = models.CharField(max_length=200,  name="Nom de la sortie")
    point_de_depart = models.CharField(max_length=200, name="Point de départ")
    description = models.CharField(max_length=1000, name="Description")
    altitude_de_depart = models.FloatField()
    altitude_min = models.FloatField()
    altitude_max = models.FloatField()
    denivele_positif_cumule = models.FloatField()
    denivele_negatif_cumule = models.FloatField()
    duree_estime = models.IntegerField(name="Durée estimée (en h)")
    CHOIX_DIFFICULTEE = ((1,"Très facile"), (2, "Facile"), (3, "Moyenne"), (4, "Difficile"), (5, "Très difficile"))
    difficulte_estimee = models.IntegerField(default=3, choices=CHOIX_DIFFICULTEE)

    def __str__(self):
        return self.titre

class Sortie(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    itineraire = models.ForeignKey("Itineraire", on_delete=models.CASCADE)
    date_sortie = models.DateField()
    duree_reelle = models.IntegerField(name="Durée réelle (en h)")
    CHOIX_DIFFICULTEE = ((1,"Très facile"), (2, "Facile"), (3, "Moyenne"), (4, "Difficile"), (5, "Très difficile"))
    difficulte_estimee = models.IntegerField(default=3, choices=CHOIX_DIFFICULTEE)

    def __str__(self):
        return self.itineraire.titre