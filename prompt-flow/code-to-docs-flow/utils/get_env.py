from dotenv import load_dotenv
import os

class GetEnv:
    def __init__(self: 'GetEnv') -> None:
        load_dotenv()
        self.__AZURE_OPENAI_SERVICE = os.getenv('AZURE_OPENAI_SERVICE')
        self.__AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
        self.__AZURE_OPENAI_TOKEN = os.getenv('AZURE_OPENAI_TOKEN')
        self.__AZURE_OPENAI_DEPLOYMENT = os.getenv('AZURE_OPENAI_DEPLOYMENT')

    def service_name(self: 'GetEnv') -> str:
        return self.__AZURE_OPENAI_SERVICE or ''
    
    def api_version(self: 'GetEnv') -> str:
        return self.__AZURE_OPENAI_API_VERSION or ''
    
    def token(self: 'GetEnv') -> str:
        return self.__AZURE_OPENAI_TOKEN or ''
    
    def deployment(self: 'GetEnv') -> str:
        return self.__AZURE_OPENAI_DEPLOYMENT or ''
