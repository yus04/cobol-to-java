from promptflow.core import tool
from utils.extract_code import ExtractCode

@tool
def extract_procedure_div(code: str) -> str:
    ec = ExtractCode(division = 'PROCEDURE', section = None)
    return ec.extract_division(code)
