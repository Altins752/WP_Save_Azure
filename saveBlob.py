#!/usr/bin/python3
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    def importBlob(fileName) :
        print("Azure Blob Storage v" + __version__)
        # Quick start code goes here
        connect_str = "DefaultEndpointsProtocol=https;AccountName=bckpwpp6oc;AccountKey=03yTYCeT3lnbyQu/yC5zAwYuMRnUI+TJ6bQPCG1Jvf6iC9PHz6ZvA4POl+8ppVj+eI3CwkpeY+Iu+AStgLaMsQ==;EndpointSuffix=core.windows.net"

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_service_client.max_single_put_file_size = 4 * 1024 * 1024
        blob_service_client.timeout=180

        # Create a unique name for the container
        container_name = "test"

        # Create a local directory to hold blob data
        local_path = "./bckp_blob"

        local_file_name = fileName
        upload_file_path = os.path.join(local_path, local_file_name)

        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

        print("\nTéléchargement vers Azure Blob de :" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, blob_type="BlockBlob", connection_timeout=600)

        
        print("Téléchargement terminé")

except Exception as ex:
    print('Exception:')
    print(ex)