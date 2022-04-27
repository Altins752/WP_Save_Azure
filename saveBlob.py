#!/usr/bin/python3
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

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
            blob_client.upload_blob(data, blob_type="BlockBlob", connection_timeout=600)


        print("Téléversement terminé")

    except Exception as ex:
        print('Exception:')
        print(ex)


# fonction pour la supression de l'archive d'il y a 5 jours sur Azure blob
def deletBlob(fileName, connect_str, container_name) :
    try:
        # création de l'objet BlobServiceClient utilisé pour interragir avec les containers Azure
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # créez un client blob en utilisant le nom du fichier local comme nom du blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        try:
            # supression de l'archive sur Azure Blob
            print("\nSupression du Blob : " + fileName)
            blob_client.delete_blob()
            print("Supression terminée")
        except Exception as ex:
            print('Le blob n\'existe pas')

    except Exception as ex:
        print('Exception:')
        print(ex)

    