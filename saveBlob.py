#!/usr/bin/python3
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


def importBlob(fileName, local_bckp, connect_str, container_name) :
    try:
        print("Azure Blob Storage v" + __version__)
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Définition du chemin de téléversement local
        upload_file_path = f"{local_bckp}{fileName}"

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        print("\nTéléversement vers Azure Blob de : " + fileName)

        # Téléversement des données
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob", connection_timeout=600)


        print("Téléversement terminé")

    except Exception as ex:
        print('Exception:')
        print(ex)

def deletBlob(fileName, connect_str, container_name) :
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        print("\nSupression du Blob : " + fileName)
        blob_client.delete_blob()
        print("Supression terminée")

    except Exception as ex:
        print('Exception:')
        print(ex)

    