from django.db import models
from django.contrib.auth.models import User


class Itineraire(models.Model):
    """
    Un itinéraire auquel est attaché 0, 1 ou plusieurs sorties
    """
    titre = models.CharField(max_length=200)
    point_de_depart = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    altitude_de_depart = models.FloatField()
    altitude_min = models.FloatField()
    altitude_max = models.FloatField()
    denivele_positif_cumule = models.FloatField()
    denivele_negatif_cumule = models.FloatField()
    duree_estime = models.IntegerField()
    CHOIX_DIFFICULTEE = ((1,"Très facile"), (2, "Facile"), (3, "Moyenne"), (4, "Difficile"), (5, "Très difficile"))
    difficulte_estimee = models.IntegerField(default=3, choices=CHOIX_DIFFICULTEE)

    def __str__(self):
        return self.titre

class Sortie(models.Model):
    """
    Une sortie qui correspond à un utilisateur et une sortie
    """
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    itineraire = models.ForeignKey("Itineraire", on_delete=models.CASCADE)
    date_sortie = models.DateField()
    duree_reelle = models.IntegerField()
    CHOIX_DIFFICULTEE = ((1,"Très facile"), (2, "Facile"), (3, "Moyenne"), (4, "Difficile"), (5, "Très difficile"))
    difficulte_estimee = models.IntegerField(default=3, choices=CHOIX_DIFFICULTEE)

    def __str__(self):
        return f"{self.itineraire} : {self.utilisateur}"