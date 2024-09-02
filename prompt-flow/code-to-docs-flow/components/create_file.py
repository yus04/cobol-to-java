from promptflow.core import tool
from storage.account import StorageAccount
from datetime import datetime, timedelta, timezone
import os

def get_current_time() -> str:
    japan_timezone = timezone(timedelta(hours = 9))
    return datetime.now(japan_timezone).strftime("%Y-%m-%d %H:%M:%S")

def update_blob_name(storage_account: dict, file_name: str) -> dict:
    # ディレクトリ部分を取得
    directory = os.path.dirname(storage_account["blob_name"])

    # ファイル名と結合した後、Blob 名を更新
    storage_account["blob_name"] = os.path.join(directory, file_name)

    return storage_account

@tool
def create_file(storage_account: dict, data: bytes) -> str:
    # ファイル名の設定
    file_name = get_current_time() + ".md"

    # Blob 名の変更
    storage_account = update_blob_name(storage_account, file_name)

    # ストレージアカウント
    sa = StorageAccount.from_dict(storage_account)

    # Blob データのアップロード
    sa.upload_blob(data)
