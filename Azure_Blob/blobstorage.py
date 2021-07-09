  '''
@Author: Sailesh Chauhan
@Date: 09-07-2021
@Last Modified time: 09-07-2021
@Title : In this code I have used python SDK to connect with Azure Storage and creating container in Blob
         storage and uploading blobs,downloading blobs, deleting blobs.
'''
import uuid,logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from decouple import config


print("Azure Blob Storage v" + __version__ + " - Python Blob Manipulation")

connect_str = config('AZURE_STORAGE_CONNECTION_STRING')
image_path='D:\\AzureWithPython\\Azure_Blob\\Blob_Data\\Azure-1.jpg'

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def create_container(container_name,blob_service_client):
    id=str(uuid.uuid4())
    container_name = container_name+id
    container_client = blob_service_client.create_container(container_name)
    return [container_client,container_name]


def upload_file(filePath,blob_service_client,container_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_1')
    with open(filePath, "rb") as data:
        blob_client.upload_blob(data)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_2')
    blob_client.upload_blob(filePath)

def list_container(container_client):
    logging.info("\nList Of Blobs in container")
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        logging.info("\t" + blob.name)

download_file_path='D:\\AzureWithPython\\Azure_Blob\\Blob_Data\\download.jpg'

def download_file(download_file_path,container_name):
    logging.info("\n Downloading Blobs from container")
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_1')
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

def delete_container(containerId):
    containerId.delete_container()
    logging.info('Deleted succesfully   '+str(containerId))
