TP – Data Centers, Green IT et Data Science
🎯 Objectifs
Ce projet explore les enjeux énergétiques et environnementaux des data centers à travers :
L’analyse d’un dataset mondial.
La mise en place de visualisations et modèles statistiques.
Une comparaison des pratiques énergétiques par pays et continents.
L’automatisation d’un pipeline CI/CD avec GitHub Actions.


📂 Contenu du projet
TP_student.ipynb : Notebook principal contenant les analyses et visualisations.
Book1.csv : Jeu de données fourni.
requirements.txt : Liste des dépendances Python.
test_sample.py : Petit fichier de tests unitaires (Pytest).
.github/workflows/python-ci.yml : Workflow GitHub Actions pour CI/CD.
README.md : Documentation générale du projet.


🚀 Exécution locale
Cloner le repo :
git clone https://github.com/Mr10Wick/tp-data-centers.git
cd tp-data-centers
Installer les dépendances :
pip install -r requirements.txt
Lancer le notebook :
jupyter notebook TP_student.ipynb


✅ CI/CD
Un workflow GitHub Actions est configuré pour :
Installer les dépendances,
Lancer les tests unitaires (pytest),
Exécuter automatiquement le notebook avec papermill.


🌱 Green IT
L’automatisation CI/CD permet d’éviter les exécutions manuelles multiples, réduisant ainsi la consommation énergétique inutile et améliorant l’efficacité du cycle de développement.
