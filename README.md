# WP_Save_Azure
---

Script permettant la sauvegarde journalière d'un site WP sur Azure Blob avec une rétention de 5 jours

## Près requis

```pip install Azure```

## Description du fichier de configuration

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

