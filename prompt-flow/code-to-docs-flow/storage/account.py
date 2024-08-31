from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient

class StorageAccount:
    def __init__(self: 'StorageAccount', connection_string: str, container_name:str, blob_name: str) -> None:
        self.__connection_string = connection_string
        self.__container_name = container_name
        self.__blob_name = blob_name

    def _blob_service_client(self: 'StorageAccount') -> BlobServiceClient:
        return BlobServiceClient.from_connection_string(self.__connection_string)
    
    def _blob_container_client(self: 'StorageAccount') -> ContainerClient:
        return self._blob_service_client().get_container_client(self.__container_name)

    def _blob_client(self: 'StorageAccount') -> BlobClient:
        return self._blob_container_client().get_blob_client(self.__blob_name)

    def upload_blob(self: 'StorageAccount', data: bytes) -> None:
        self._blob_client().upload_blob(data)
    
    def download_blob(self: 'StorageAccount') -> bytes:
        return self._blob_client().download_blob().readall()

    # シリアライズメソッド
    def to_dict(self: 'StorageAccount') -> dict:
        return {
            "connection_string": self.__connection_string,
            "container_name": self.__container_name,
            "blob_name": self.__blob_name
        }

    # デシリアライズメソッド
    @classmethod
    def from_dict(cls: 'StorageAccount', data: dict) -> 'StorageAccount':
        return cls(
            connection_string = data.get("connection_string", ""),
            container_name = data.get("container_name", ""),
            blob_name = data.get("blob_name", "")
        )
