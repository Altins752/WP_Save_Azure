#!/usr/bin/python3
import os, syslog
from pprint import pprint
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# fonction pour l'import de l'archive sur Azure blob
def importBlob(fileName, local_bckp, connect_str, container_name) :
    try:
        
        syslog.syslog("Coucou!")

        # création de l'objet BlobServiceClient utilisé pour interragir avec les containers Azure
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # définition du chemin de téléversement local
        upload_file_path = f"{local_bckp}{fileName}"

        # créez un client blob en utilisant le nom du fichier local comme nom du blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        print("\nTéléversement vers Azure Blob de : " + fileName)

        # téléversement des données
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob", connection_timeout=600)


        print("Téléversement terminé")

    except Exception as ex:
        if ex.exc_type == "NewConnectionError" :
            syslog.syslog("connexion impossible")
            sys.exit(1)

        elif ex.error_code == "BlobAlreadyExists" :
            syslog.syslog(f'Le blob {fileName} existe déjà dans votre conteneur {container_name}')
            syslog.syslog("arrêt du script")
            exit()
            # sys.exit(2)
        else:
            print(ex.error_code)
            syslog.syslog("Erreur inconnue")
            syslog.syslog("arrêt du script")
            exit()
            # sys.exit(99)
            
        

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

    except Exception as ex:
        if ex.exc_type == "NewConnectionError" :
            syslog.syslog("connexion impossible")
            syslog.syslog("arrêt du script")
            exit()
            # sys.exit(1)
            
        elif ex.error_code == "BlobNotFound" :
            syslog.syslog(f'Le blob {fileName} ne peut pas être supprimé car il n\'existe pas dans votre conteneur {container_name} sur Azure Blob')
            error = 1
            return error
            # sys.exit(2)
        else :
            print(ex.error_code)
            syslog.syslog("Erreur inconnue")
            syslog.syslog("arrêt du script")
            exit()
            # sys.exit(99)   

    
        


    
    