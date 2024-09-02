class SplitCode:
    def __init__(self: 'SplitCode', code: str) -> None:
        self.__code = code
    
    def split_by_entry(self: 'SplitCode') -> list[str]:
        splited_code, item = [], []
        for line in self.__code.strip().split('\n'):
            splited_code, item = self._append_splited_code_and_item(line, splited_code, item)
        return self._final_append(splited_code, item)

    def _append_splited_code_and_item(
            self: 'SplitCode', line: str, splited_code: list[str], item: list[str]
        ) -> tuple[list[str], list[str]]:
        if 'ENTRY' in line and item != []:
            splited_code.append('\n'.join(item))
            item = []
        item.append(line)
        return splited_code, item
    
    def _final_append(self: 'SplitCode', splited_code: list[str], item: list[str]) -> list[str]:
        if item != []: splited_code.append('\n'.join(item))
        return splited_code
