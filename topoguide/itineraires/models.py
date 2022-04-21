from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Itineraire(models.Model):
    """
    Un itinéraire auquel est attaché 0, 1 ou plusieurs sorties
    """
    titre = models.CharField(max_length=200)
    point_de_depart = models.CharField(max_length=200)
    description = models.TextField()
    altitude_de_depart = models.FloatField(validators=[validators.MinValueValidator(0)])
    altitude_min = models.FloatField(validators=[validators.MinValueValidator(0)])
    altitude_max = models.FloatField(validators=[validators.MinValueValidator(0)])
    denivele_positif_cumule = models.FloatField(validators=[validators.MinValueValidator(0)])
    denivele_negatif_cumule = models.FloatField(validators=[validators.MinValueValidator(0)])
    duree_estime = models.FloatField(validators=[validators.MinValueValidator(0)])
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
    duree_reelle = models.FloatField(validators=[validators.MinValueValidator(0)])
    nombre_participant = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    CHOIX_EXPERIENCE = (("debutants", "debutants"), ("tous expérimentés", "tous expérimentés"), ("mixte","mixte"))
    experience_groupe = models.CharField(default="mixte", choices=CHOIX_EXPERIENCE, max_length=200)
    CHOIX_METEO = (("bonne","bonne"), ("moyenne","moyenne"), ("mauvaise", "mauvaise"))
    meteo = models.CharField(default="bonne", choices=CHOIX_METEO, max_length=200)
    CHOIX_DIFFICULTEE = ((1,"Très facile"), (2, "Facile"), (3, "Moyenne"), (4, "Difficile"), (5, "Très difficile"))
    difficulte_estimee = models.IntegerField(default=3, choices=CHOIX_DIFFICULTEE)

    def __str__(self):
        return f"{self.itineraire} : {self.utilisateur}"