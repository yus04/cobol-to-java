from promptflow.core import tool

@tool
def merge_file(identification_docs: str, environment_docs: str, data_docs: str, procedure_docs: str) -> str:
    identification_docs = add_heading("Identification", identification_docs)
    environment_docs = add_heading("Environment", environment_docs)
    data_docs = add_heading("Data", data_docs)
    procedure_docs = add_heading("Procedure", procedure_docs)
    return '\n'.join([identification_docs, environment_docs, data_docs, procedure_docs])

def add_heading(div_type: str, docs: str) -> str:
    header = f"# {div_type} Division の説明\n"
    return '\n'.join([header, docs])
