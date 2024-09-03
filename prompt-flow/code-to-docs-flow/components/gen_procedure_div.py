from promptflow.core import tool
from utils.extract_code import ExtractCode
from utils.split_code import SplitCode
from utils.get_env import GetEnv
from ai.aoaiclient import AOAIClient

@tool
def gen_procedure_div(system_message: str, user_message: str) -> str:
    extracted_code = user_message
    sc = SplitCode(extracted_code)
    splited_code = sc.split_by_entry()
    ge = GetEnv()
    aoaic = AOAIClient(ge.service_name(), ge.api_version(), ge.token(), ge.deployment())
    docs = add_header([])
    for code in splited_code:
        doc = aoaic.chat_completions_create(system_message, code)
        docs.append(doc)
    return '\n'.join(docs)

def add_header(item: list[str]) -> list[str]:
    item.append("| 処理概要 | コード | 処理説明 |")
    item.append("|---|---|---|")
    return item
