#!/usr/bin/python3
import os, logging, sys
import logging.config
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Configuration logging
logging.config.fileConfig('logging.conf')

myLog = logging.getLogger('SaveBlobAzureScript')

# fonction pour l'import de l'archive sur Azure blob
def importBlob(fileName, local_bckp, connect_str, container_name) :
    try:
        # création de l'objet BlobServiceClient utilisé pour interragir avec les containers Azure
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # définition du chemin de téléversement local
        upload_file_path = f"{local_bckp}{fileName}"

        # créez un client blob en utilisant le nom du fichier local comme nom du blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        print("\nTéléversement vers Azure Blob de : " + fileName)

        # téléversement des données
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob", connection_timeout=60)


        print("Téléversement terminé")

# exception pour gérer les erreurs
    except Exception as ex:
        if ex.exc_type == "NewConnectionError" :
            myLog.error("connexion impossible")
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()

        elif ex.error_code == "BlobAlreadyExists" :
            myLog.error(f'Le blob {fileName} existe déjà dans votre conteneur {container_name}')
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()

        elif ex.error_code == "ContainerNotFound" :
            myLog.error(f'Le conteneur {container_name} n\'existe pas sur Azure Blob')
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()

        else:
            print(ex.error_code)
            myLog.error("Erreur inconnue")
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()
            
        

# fonction pour la supression de l'archive sur Azure blob suivant le nombre de jours configuré
def deletBlob(fileName, connect_str, container_name) :
    try:
        # création de l'objet BlobServiceClient utilisé pour interragir avec les containers Azure
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # créez un client blob en utilisant le nom du fichier local comme nom du blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        # supression de l'archive sur Azure Blob
        print("\nSupression du Blob : " + fileName)
        blob_client.delete_blob()
        print("Supression terminée")

# exception pour gérer les erreurs
    except Exception as ex:
        if ex.exc_type == "NewConnectionError" :
            myLog.error("connexion impossible")
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()
            
        elif ex.error_code == "BlobNotFound" :
            myLog.warning(f'Le blob {fileName} ne peut pas être supprimé car il n\'existe pas dans votre conteneur {container_name} sur Azure Blob')
            error = 1
            return error

        elif ex.error_code == "ContainerNotFound" :
            myLog.error(f'Le conteneur {container_name} n\'existe pas sur Azure Blob')
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()

        else :
            print(ex.error_code)
            myLog.error("Erreur inconnue")
            myLog.info("arrêt du script")
            sys.exit(2)
            exit()  

    
        


    
    