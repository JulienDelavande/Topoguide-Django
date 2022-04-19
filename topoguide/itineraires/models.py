from django.db import models

class Intineraire(models.Model, name="Nom de la sortie"):
    titre = models.CharField(max_length=200)
    point_de_depart = models.CharField(max_length=200, name="Point de départ")
    description = models.CharField(max_length=1000, name="Description")
    altitude_de_depart = models.FloatField()
    altitude_min = models.FloatField()
    altitude_max = models.FloatField()
    denivele_positif_cumule = models.FloatField()
    denivele_negatif_cumule = models.FloatField()
    duree_estime = models.IntegerField(name="Durée estimée (en h)")
    difficulte_estimee = models.IntegerField(choices=[1,2,3,4,5])

class Sortie(models.Model):
    #utilisateur = models.ForeignKey("User", on_delete=models.CASCADE)
    itineraire =models.ForeignKey("Itineraire", on_delete=models.CASCADE)
    date_sortie = models.DateField()
    duree_reelle = models.IntegerField(name="Durée réelle (en h)")
    difficulte_estimee = models.IntegerField(choices=[1,2,3,4,5])