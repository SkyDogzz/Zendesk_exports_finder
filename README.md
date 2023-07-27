# Extraction des Notes de Satisfaction depuis Zendesk Export

Ce script Python est conçu pour extraire les notes de satisfaction à partir d'un export Zendesk et les enregistrer dans un fichier CSV. Le programme est exécuté dans un conteneur Docker pour faciliter son déploiement et son utilisation.
## Prérequis

Avant d'exécuter le script, assurez-vous que vous avez les éléments suivants :

1. Fichier d'export Zendesk : Assurez-vous d'avoir exporté les données Zendesk dans un fichier au format JSON.

2. Fichier .env : Créez un fichier .env dans le même répertoire que le script, et définissez les variables d'environnement requises :

```bash
    makefile

    ZENDESK_EXPORT_FILENAME=<nom_du_fichier_export>
    ZENDESK_EXPORT_FILENAME_REPAIRED=<nom_du_fichier_export_repare>
    SEARCH=<mot_cle_recherche_1>
    SEARCH2=<mot_cle_recherche_2>
```
Remplacez <nom_du_fichier_export> par le nom de votre fichier d'export Zendesk, <nom_du_fichier_export_repare> par le nom du fichier où vous souhaitez enregistrer les données filtrées, <mot_cle_recherche_1> par le premier mot-clé de recherche et <mot_cle_recherche_2> par le deuxième mot-clé de recherche.

3. Docker et Docker Compose : Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.

## Instructions

1. Clonez ce dépôt Git ou copiez le fichier Python et le fichier .env dans votre répertoire de travail.

2. Placez votre fichier d'export Zendesk au format JSON dans le même répertoire que le script Python.

3. Modifiez le fichier .env pour définir les variables d'environnement requises.

4. Ouvrez un terminal ou une invite de commande et exécutez la commande suivante pour lancer le programme :

```bash
docker-compose up
ou
docker compose up
```

Le programme s'exécutera et traitera l'export Zendesk pour extraire les notes de satisfaction. Une fois terminé, le conteneur s'arrêtera automatiquement.

5. Le fichier CSV résultant sera disponible dans le répertoire de travail sous le nom resultat.csv. Ce fichier contiendra les colonnes URL, ID, Name, Email, Note et Date, où Note représente la note de satisfaction extraite et Date représente la date associée à la note.

## Remarques

- Le script utilise la bibliothèque dotenv pour charger les variables d'environnement à partir du fichier .env. Assurez-vous que les dépendances requises sont installées en exécutant pip install python-dotenv. Cette commande est censé être effectué automatiquement lors du build du Dockerfile.

- Le script utilise également les bibliothèques csv et json pour la manipulation des données.

- Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à ouvrir une nouvelle question dans ce dépôt Git.