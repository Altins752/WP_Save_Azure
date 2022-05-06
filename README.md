# Save_Blob_Azure_Script

Script permettant la sauvegarde journalière (manuelle/automatique) de fichiers et d'une base de donnée local et l'important ensuite dans un Blob Azure.

## Près requis

* Utilisation de python 3.9.2

## Utiliser Save_Blob_Azure_Script

1. Télécharger le dépôt complets du projet
2. Attribuer les droits necessaire aux scripts python
3. Installer les bibliothèque se trouvant dans `requirement.txt` : 

        pip install -r requirement.txt

4. [Compléter](#Description_config) le fichier de configuration ```config.sample``` et renommer le en ```config```
5. Pour executer le script manuellement il vous suffis d'effectuer cette commande dans le répertoire où vous avez télécharger les fichiers: ```python3 main.py```
6. Pour que le script s'effectue tous les jours automatiquement, il faut créer une entrée cron executant une fois par jours la commande ```python3 <chemin absolue vers le repertoire des scripts>/main.py``` 


## code de sortie

| Code de sortie |                 Signification                  |
|:---------------|:----------------------------------------------:|
| 0              |     Le script s'est terminer sans erreurs      |
| 1              | Le script s'est terminer mais avec des erreurs |
| 2              |   Le script a été interrompue par une erreur   |

## Logs

Le fichier de logs et généré au premier lancement du programme. Il se nomme "SaveBlobAzureScript.log" et est stocké dans le répertoire du script.


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
* **day_retention** : Nombres de jours de conservation des sauvegardes

