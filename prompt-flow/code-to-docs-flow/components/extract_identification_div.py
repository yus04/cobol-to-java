from promptflow.core import tool
from utils.extract_code import ExtractCode

@tool
def extract_identification_div(code: str) -> str:
    ec = ExtractCode(division = 'IDENTIFICATION', section = None)
    return ec.extract_division(code)
