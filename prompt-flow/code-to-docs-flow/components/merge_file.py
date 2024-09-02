from promptflow.core import tool

@tool
def merge_file(identification_docs: str, environment_docs: str, data_docs: str, procedure_docs: str) -> str:
    return '\n'.join([identification_docs, environment_docs, data_docs, procedure_docs])
