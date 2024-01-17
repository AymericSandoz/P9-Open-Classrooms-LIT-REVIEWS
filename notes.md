N’oubliez pas : générez et exécutez les migrations seulement après avoir configuré votre modèle User personnalisé. Sinon, vous devrez supprimer les migrations, supprimer la base de données (ou supprimer le fichierdb.sqlite3 ), et les générer et exécuter à nouveau.

Dans static(cd reviews, cd static)

sass sass/styles.scss css/styles.css

Ou

sass --watch sass/styles.scss:css/styles.css

cd reviews_project
env/Scripts/activate
cd reviews
python manage.py runserver

aller à http://127.0.0.1:8000/

FLake 8 rapport
pip install flake8
flake8 --statistics --output-file=flake8_report.txt

ou pour html
pip install flake8-html
flake8 --format=html --htmldir=flake8_report

A faire :
S'occuper de la gestion des erreurs
Accessibilité
style de la page d'acceuil
Responsive
MEttre les bon noms de varibale dans models
bloquer un utilisateur.
"Aucun fichier n'a été ajouté"

QUestions
Dans rechercher comment faire pour rechercher uniquement dans les fichiers conçu par moi même
FOrm et erreurs
"Aucun fichier n'a été ajouté"

Qu'entendent t'il par(page 3)
Un utilisateur peut suivre d'autres utilisateurs pour voir leurs critiques (ce qu’ils
demandent et ce qu’ils postent). Il n’est pas nécessaire de créer un système
complexe de suivi pour ce projet (flux Discover ou recherche d’utilisateurs).

QUe faire pour l'accessibité
QUestion de droit d'auteur pour une application ?

Utilisez un outil de vérification d'accessibilité : Il existe des outils en ligne, comme WAVE (Web Accessibility Evaluation Tool), qui peuvent analyser votre site et identifier les problèmes d'accessibilité.

Respectez les standards HTML : Assurez-vous que votre code HTML est propre et valide. Utilisez le validateur HTML du W3C pour vérifier si votre code respecte les standards.

Textes alternatifs pour les images : Fournissez des textes alternatifs descriptifs pour toutes les images, afin que les lecteurs d'écran puissent les interpréter pour les utilisateurs malvoyants.

Contrastes de couleurs suffisants : Vérifiez que les couleurs de votre site offrent un contraste suffisant, particulièrement pour le texte et les éléments d'interface.

Utilisation correcte des en-têtes : Structurez votre contenu en utilisant correctement les balises d'en-tête (H1, H2, etc.) pour une meilleure compréhension par les lecteurs d'écran.

Navigation au clavier : Assurez-vous que votre site peut être navigué entièrement au clavier, sans nécessiter l'utilisation de la souris.

Étiquettes de formulaire accessibles : Assurez-vous que tous les champs de formulaire sont correctement étiquetés pour faciliter leur utilisation par des logiciels de lecture d'écran.

Gestion du multimédia : Pour le contenu multimédia, comme les vidéos, assurez-vous de fournir des sous-titres et des descriptions audio.

Responsive Design : Votre site doit être accessible et fonctionnel sur une variété d'appareils, y compris les mobiles.

Testez avec de vrais utilisateurs : Enfin, il est utile de tester votre site avec de vrais utilisateurs, y compris ceux qui ont des handicaps, pour obtenir des retours directs sur l'accessibilité.

NOtes pour réponses aux questions de sécurité :
Les mots de passe en base de données sont chiffrés ;
La modification ou la suppression d’un billet ou commentaire est réservée à son auteur ;
Les vérifications faites en front-end sont également faites en back-end.

Note pour réponse à l'accessibilité
J'ai utiliser outils wave
Les images ont toutes un titre et un texte alternatif ;
Le design ne propose pas une différence de contraste trop faible entre le fond et le contenu…
Les liens ont un titre explicite.

Maj 12/01
Faire le Readme
Verifier le shema de donnees
Faire respecter les directives PEP8 et passe un linter PEP8 ;
le code respecte des principes de sécurité, d’ergonomie et de navigabilité ; sécurité ?

l’étudiant sait expliquer son architecture, ses conventions de nommage et comment il a suivi les recommandations de Django en matière de bonnes pratiques ;
l’étudiant sait expliquer comment il a pris en compte les principes de sécurité, d’ergonomie et de navigabilité.

l’interface respecte les bonnes pratiques d'accessibilité du référentiel WCAG

Normalement django gère les injections
