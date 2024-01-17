# Readme - Application de Critiques de Livres et d'Articles.

Projet réalisé dans le cadre d'une alternance de développeur python.
Cette application offre une plateforme pour publier et demander des critiques sur des livres ou des articles.. Voici un guide pour installer et exécuter le projet Django.

## Installation et lancement

Suivez ces étapes pour installer le projet Django sur votre machine :

1. **Cloner le Répertoire :** `git clone https://github.com/AymericSandoz/P9-Open-Classrooms-LIT-REVIEWS.git`

2. **Accéder au Répertoire :** `cd reviews_project`

3. **Créer un Environnement Virtuel :** `python -m venv venv`

4. **Activer l'Environnement Virtuel :**

   - Sur Windows : `venv\Scripts\activate`
   - Sur macOS/Linux : `source venv/bin/activate`

5. **Installer les Dépendances :** `pip install -r requirements.txt`

6. **Appliquer les Migrations :** `python manage.py migrate`

7. **Accéder au répertoire :** `cd reviews`

8. **Lancer le Serveur de Développement :** `python manage.py runserver`

9. **Lancer sass :** `cd reviews_projectstatic` `sass --watch sass/styles.scss:css/styles.css`

10. **Accéder à l'Application :** Ouvrez votre navigateur et allez à [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Générer un rapport flake 8

`flake8 --format=html --htmldir=flake8_report .\reviews\authentication\forms.py .\reviews\authentication\views.py .\reviews\authentication\models.py .\reviews\reviews_app\forms.py .\reviews\reviews_app\views.py .\reviews\reviews_app\migrations\ .\reviews\reviews\urls.py`
