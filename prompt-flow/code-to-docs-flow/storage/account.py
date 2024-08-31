class StorageAccount:
    def __init__(self: 'StorageAccount', connection_string: str, container_name:str, blob_name: str) -> None:
        self.__connection_string = connection_string
        self.__container_name = container_name
        self.__blob_name = blob_name
    
    def get_connection_string(self: 'StorageAccount') -> str:
        return self.__connection_string

    def get_container_name(self: 'StorageAccount') -> str:
        return self.__container_name

    def get_blob_name(self: 'StorageAccount') -> str:
        return self.__blob_name

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
