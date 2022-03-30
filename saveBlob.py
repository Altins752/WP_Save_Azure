import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "bckptest"

    # Create a local directory to hold blob data
    local_path = "./bckp_blob"

    local_file_name = "test.txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    print(upload_file_path)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    blob_client.upload_blob(upload_file_path)

    
    print("upload done")

except Exception as ex:
    print('Exception:')
    print(ex)
    print(data)