# topoguide-julien-delavande

Application pour les randonneurs

->Dépendances:
-django
-django-bootstrap-v5


->Quelques identifiants et mdp

Identifiant:Julien
mdp:mdp
status:superuser (accès à l'admin)

Identifiant:Toto
mdp:mdp12345
status:user


->Rapide description

Un utilisateur non connecté pourra:
-se connecter à l'aide du bouton Connexion dans la barre de navigation
-Regarder la liste des itinéraires disponibles (page /itinéraires/)
-Regarder la liste des sorties pour un itinéraire en particulier (page /itinéraires/<id de l itinéraire>/ListeSorties/)
-Regarder le détail d'une sortie en particulier(/itinéraires/<id de l itinéraire>/ListeSorties/<id de la sortie>)

Un utilsateur connecté pourra:
-Se déconnecter à l'aide du bouton Déconnexion dans la barre de navigation
-Se logguer sous un autre utilisateur en cliquant sur son nom d'utilisateur
-Regarder la liste des itinéraires disponibles (page /itinéraires/)
-Regarder la liste des sorties pour un itinéraire en particulier (page /itinéraires/<id de l itinéraire>/ListeSorties/)
-Regarder le détail d'une sortie en particulier(/itinéraires/<id de l itinéraire>/ListeSorties/<id de la sortie>)
-Ajouter une sortie (/itinéraires/AjouterModifierSortie)
-Modifier une sortie qu'il aurait saisie (/itinéraires/AjouterModifierSortie)
