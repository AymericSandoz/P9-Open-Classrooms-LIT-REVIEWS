N’oubliez pas : générez et exécutez les migrations seulement après avoir configuré votre modèle  User  personnalisé. Sinon, vous devrez supprimer les migrations, supprimer la base de données (ou supprimer le fichierdb.sqlite3  ), et les générer et exécuter à nouveau.


sass style/styles.scss static/css/styles.css

python manage.py collectstatic


env/Scripts/activate
cd review
python manage.py runserver

aller à http://127.0.0.1:8000/