# WP_Save_Azure
---

Script permettant la sauvegarde journalière (manuelle/automatique) de fichiers et d'une base de donnée local et l'important ensuite dans un Blob Azure.

*Sur Azure, il y as une rétention de 5 jours.*

## Près requis

* Utilisation de python 3.9.2
* Installer la bibliothèque Azure pour python :

        pip install Azure


## Utiliser Save_Blob_Azure_Script

1. Télécharger le dépôt complets du projet
2. Attribuer les droits necessaire aux scripts python
3. [Compléter](#Description_config) le fichier de configuration ```config_sample``` et renommer le en ```config```
4. pour executer le script manuellement il vous suffis d'effectuer cette commande dans le répertoire où vous avez télécharger les fichiers: ```python3 main.py```
5. Pour que le script s'effectue tous les jours automatiquement, il faut créer une entrée cron executant une fois par jours la commande ```python3 \< *chemin absolue vers le repertoire des scripts* \>/main.py`` 

## Description du fichier de configuration<a name="Description_Config"></a>

### BDD
* **bddid** : identifiant de la base de données
* **bddmdp** : mot de passe de la base de donnée
* **bddname** : nom de la base de donnée

### Azure
* **connect_string**: clès de connexion à récupérer sur le compte azure ([aide](https://docs.microsoft.com/fr-fr/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows#copy-your-credentials-from-the-azure-portal))
* **container_name** : Nom du containers azure ou seront stocké les sauvegardes

### FILES
* **folder_path** : Chemin absolu vers le dossier contenant les fichiers à sauvegarder
* **local_Backup** : Chemin absolu vers le dossier conservant une sauvagarde local

