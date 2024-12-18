# SmartLink - Application de Liens Personnalisés

SmartLink est une application web permettant de créer une page de liens personnalisés, semblable à des "smart links" utilisés par des artistes, créateurs de contenu, ou toute personne souhaitant regrouper ses liens en un seul endroit facile d'accès.

## Fonctionnalités

- Affichage de liens personnalisés : Vous pouvez ajouter des liens (URL) pour rediriger les utilisateurs vers vos profils ou contenus en ligne (Spotify, YouTube, etc.).
- Statistiques : Le nombre de clics sur chaque lien est enregistré pour vous permettre de suivre l'interaction avec vos liens.
- Responsive : L'application est conçue pour être utilisée sur desktop et mobile avec un design moderne et épuré.

## Technologies Utilisées

- **Flask** : Framework web Python pour développer l'application.
- **SQLite** : Base de données légère pour stocker les liens et leurs statistiques.
- **HTML, CSS** : Langages utilisés pour structurer et styliser la page.
- **FontAwesome** : Utilisé pour les icônes des liens (YouTube, Spotify, etc.)

## Installation

### Prérequis

Avant d'exécuter l'application localement, assurez-vous d'avoir les outils suivants installés :

- **Python** 3.6 ou supérieur : [Télécharger Python](https://www.python.org/downloads/)
- **Git** : [Télécharger Git](https://git-scm.com/downloads)

### Étapes d'Installation

1. Clonez ce dépôt sur votre machine locale :

    Créez un environnement virtuel pour isoler les dépendances :

python3 -m venv venv

    Activez l'environnement virtuel :
        Sur Windows : venv\Scripts\activate
        Sur macOS/Linux : source venv/bin/activate

    Installez les dépendances nécessaires :

pip install -r requirements.txt

    Créez la base de données et les tables :

python
from app import create_db
create_db()

    Lancez l'application Flask :

python app.py

L'application sera accessible à l'adresse suivante dans votre navigateur : http://127.0.0.1:5000/
Déploiement


Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, voici comment vous pouvez contribuer :

    Fork ce dépôt.
    Créez une branche pour votre fonctionnalité (git checkout -b feature/nom-de-la-fonctionnalité).
    Commitez vos modifications (git commit -m 'Ajout d'une nouvelle fonctionnalité').
    Poussez la branche (git push origin feature/nom-de-la-fonctionnalité).
    Ouvrez une pull request.

Auteurs

    Ton Nom : Yannick Sica




