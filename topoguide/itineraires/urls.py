from django.urls import path
from . import views

app_name = 'itineraires'
urlpatterns = [
    path('', views.listeItineraires, name='listeItineraires'),
    path('<int:itineraire_id>/', views.listeSorties, name='listeSorties'),
    path('sortieDetails/<int:sortie_id>', views.sortieDetails, name='sortieDetails'),
    path('ajouterModifSortie/<int:sortie_id>/', views.ajouterModifSortie, name='ajouterModifSortie'),
]