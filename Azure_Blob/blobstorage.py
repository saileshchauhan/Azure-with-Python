'''
@Author: Sailesh Chauhan
@Date: 09-07-2021
@Last Modified time: 09-07-2021
@Title : In this code I have used python SDK to connect with Azure Storage and creating container in Blob
         storage and uploading blobs,downloading blobs, deleting blobs.
'''
import uuid,logging,sys
sys.path.append('D:\AzureWithPython')
import logconfig
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from decouple import config


print("Azure Blob Storage v" + __version__ + " - Python Blob Manipulation")

connect_str = config('AZURE_STORAGE_CONNECTION_STRING')
image_path=config('image_path')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def create_container(container_name,blob_service_client):
    '''
    Description:
        Method creates container in storage account.
    Parameters:
        container_name, blob_service_client
    Returns:
        None.
    '''
    try:
        id=str(uuid.uuid4())
        container_name = container_name+id
        container_client = blob_service_client.create_container(container_name)
        return [container_client,container_name]
    except Exception as x:
        logging.info(str(x))

def upload_file(filePath,blob_service_client,container_name):
    '''
    Description:
        Method upload file as image to the container.
    Parameters:
        filePath,blob_service_client,container_name
    Returns:
        None.
    '''
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_1')
        with open(filePath, "rb") as data:
            blob_client.upload_blob(data)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_2')
        blob_client.upload_blob(filePath)
    except Exception as x:
        logging.info(str(x))

def list_container(container_client):
    '''
    Description:
        Method enlist container inside storage account.
    Parameters:
        container_client. 
    Returns:
        None.
    '''
    try:
        logging.info("\nList Of Blobs in container")
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            logging.info("\t" + blob.name)
    except Exception as x:
        logging.info(str(x))

download_file_path=config('download_file_path')
def download_file(download_file_path,container_name):
    '''
    Description:
        Method downloads file from the given container name.
    Parameters:
        download_file_path,container_name.
    Returns:
        None.
    '''
    try:
        logging.info("\n Downloading Blobs from container")
        blob_client = blob_service_client.get_blob_client(container=container_name, blob='Blob_1')
        with open(download_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
    except Exception as x:
        logging.info(str(x))

def delete_container(containerId):
    '''
    Description:
        Method deletes the created container at Azure portal.
    Parameters:
        containerId
    Returns:
        None.
    '''
    try:
        containerId.delete_container()
        logging.info('Deleted succesfully   '+str(containerId))
    except Exception as x:
        logging.info(str(x))

def main():
    try:
        containerList=create_container('container1',blob_service_client)
        upload_file(image_path,blob_service_client,containerList[1])
        list_container(containerList[0])
        download_file(download_file_path,containerList[1])
        delete_container(containerList[0])
    except Exception as ex:
        logging.info(ex)

if __name__=='__main__':
    main()