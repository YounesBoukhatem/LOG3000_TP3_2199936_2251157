## Nom du projet
Flask Calculator

## Numéro d'équipe
Numéro d’équipe : 23

## Objectif
Ce projet est une application web de calculatrice développée avec Flask (Python).  
La base de code initiale est partiellement fonctionnelle et nécessite une organisation, documentation et correction de bogues.  

L’objectif de ce devoir est de :  
1. Configurer correctement le projet sur GitHub pour faciliter la collaboration.  
2. Documenter chaque composant du projet (frontend, backend).  
3. Tester et corriger les bogues dans le code existant.  
4. Mettre en place un workflow Git avec branches et Pull Requests pour la gestion des modifications.  

## Prérequis d'installation
- Git 
- Python (https://www.python.org/downloads/)

## Instructions d'installations
1. Cloner le dépôt (git clone https://github.com/YounesBoukhatem/LOG3000_TP3_2199936_2251157)
2. Se mettre sur le dépot et créer un environnement virtuel (python -m venv venv)
3. Activer l'environnement virtuel (. venv/bin/activate)
4. Installer Flask (pip install flask)

## Utilisation de l'application
1. Lancer le projet (python src/app.py)
2. Si le navigateur web ne s'est pas ouvert automatiquement, naviger au lien http://127.0.0.1:5000
3. L'interface utilisateur devrait afficher une calculatrice. Voici les étapes de calcul:
    1. Cliquez sur les boutons de chiffres pour former un nombre de longueur arbitraire (correspondant à l'opérande de gauche).
    2. Cliquez sur une des opérations de la calculatrice (+, -, *, /).
    3. Répétez l'étape 1. pour former un nombre correspondant à l'opérande de droite.
    4. Cliquez sur le bouton d'égalité (=).
    5. Le résultat du calcul s'affiche dans l'écran de la calculatrice. Vous pouvez utiliser le résultat comme opérande de gauche dans les calculs subséquents en répétant les étapes 2. à 4. autant de fois que nécessaire.
    6. Pour effacer le résultat de l'écran, cliquez sur le bouton C (clear display).
4. Afin de fermer l'application, appuyez sur crtl-C tout en étant dans la console.
5. Désactivez l'environnement virtuel au besoin (deactivate).

## Tests
TODO: Une section sur les tests (comment exécuter les tests que vous ajouterez plus tard).

## Contribution
TODO: Une section sur le flux de contribution (branches, PR, issues).