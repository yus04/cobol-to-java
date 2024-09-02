class ExtractCode:
    def __init__(self: 'ExtractCode', division: str, section: str) -> None:
        self.__division = division
        self.__section = section

    def extract_division(self: 'ExtractCode', code: str) -> str:
        extracted_codes = []
        is_division = False
        is_section =  False
    
        for line in code.strip().split('\n'):
            is_division = self._check_division_in_line(is_division, line)
            is_section = self._check_section_in_line(is_section, line)

            if is_division and is_section:  
                extracted_codes.append(line)
    
        return '\n'.join(extracted_codes)

    # 対象 division であるかどうかを確認
    def _check_division_in_line(self: 'ExtractCode', is_division: bool, line: str) -> bool:
        if 'DIVISION' in line and self.__division in line:
            is_division = True 
        elif 'DIVISION' in line and not self.__division in line:
            is_division = False
        return is_division

    # 対象 section であるかどうかを確認
    def _check_section_in_line(self: 'ExtractCode', is_section: bool, line: str) -> bool:
        if self.__section == None:
            is_section = True
        elif 'SECTION' in line and self.__section in line:
            is_section = True 
        elif 'SECTION' in line and not self.__section in line:
            is_section = False
        return is_section
