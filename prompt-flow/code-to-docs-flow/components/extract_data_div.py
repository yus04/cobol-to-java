from promptflow.core import tool
from utils.extract_code import ExtractCode

@tool
def extract_data_div(code: str) -> str:
    ec = ExtractCode(division = 'DATA', section = None)
    return ec.extract_division(code)
