from promptflow.core import tool
from utils.extract_code import ExtractCode

@tool
def extract_environment_div(code: str) -> str:
    ec = ExtractCode(division = 'ENVIRONMENT', section = None)
    return ec.extract_division(code)
