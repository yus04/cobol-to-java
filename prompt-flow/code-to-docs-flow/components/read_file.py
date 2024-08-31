from promptflow import tool
from azure.storage.blob import BlobServiceClient
from storage.account import StorageAccount

@tool
def read_file(storage_account: dict) -> str:
    # ストレージアカウント情報
    sa = StorageAccount.from_dict(storage_account)
    connection_string = sa.get_connection_string()
    container_name = sa.get_container_name()
    blob_name = sa.get_blob_name()

    # BlobServiceClient の作成
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # コンテナクライアントの取得
    container_client = blob_service_client.get_container_client(container_name)

    # Blob クライアントの取得
    blob_client = container_client.get_blob_client(blob_name)

    # Blob データのダウンロード
    downloaded_blob = blob_client.download_blob().readall()

    # Blob データのデコード
    file_content = downloaded_blob.decode('shift_jis')

    return file_content
