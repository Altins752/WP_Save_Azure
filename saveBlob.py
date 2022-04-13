#!/usr/bin/python3
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


def importBlob(fileName) :
    try:
        print("Azure Blob Storage v" + __version__)
        # Quick start code goes here
        connect_str = "DefaultEndpointsProtocol=https;AccountName=bckpwpp6oc;AccountKey=03yTYCeT3lnbyQu/yC5zAwYuMRnUI+TJ6bQPCG1Jvf6iC9PHz6ZvA4POl+8ppVj+eI3CwkpeY+Iu+AStgLaMsQ==;EndpointSuffix=core.windows.net"

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Définition du container sur Azure et di chemin de téléversement local
        container_name = "test"
        upload_file_path = f"./bckp_blob/{fileName}"

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

def deletBlob(fileName) :
    try:
        connect_str = "DefaultEndpointsProtocol=https;AccountName=bckpwpp6oc;AccountKey=03yTYCeT3lnbyQu/yC5zAwYuMRnUI+TJ6bQPCG1Jvf6iC9PHz6ZvA4POl+8ppVj+eI3CwkpeY+Iu+AStgLaMsQ==;EndpointSuffix=core.windows.net"
        container_name = "test"
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=fileName)

        print("\nSupression du Blob : " + fileName)
        blob_client.delete_blob()
        print("Supression terminée")
        
    except Exception as ex:
        print('Exception:')
        print(ex)

    