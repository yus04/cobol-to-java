from promptflow import tool
from storage.account import StorageAccount

@tool
def read_file(storage_account: dict) -> str:
    # ストレージアカウント
    sa = StorageAccount.from_dict(storage_account)

    # Blob データのダウンロードとデコード
    file_content = sa.download_blob().decode('shift_jis')

    return file_content
