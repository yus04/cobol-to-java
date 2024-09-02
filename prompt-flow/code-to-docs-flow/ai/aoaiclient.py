from openai import AzureOpenAI

class AOAIClient:
    def __init__(
            self, AZURE_OPENAI_SERVICE: str, AZURE_OPENAI_API_VERSION: str, 
            AZURE_OPENAI_TOKEN: str, AZURE_OPENAI_DEPLOYMENT: str
        ) -> None:
        self.__AZURE_OPENAI_DEPLOYMENT = AZURE_OPENAI_DEPLOYMENT
        self.__openai_client = AzureOpenAI(
            azure_endpoint = f"https://{AZURE_OPENAI_SERVICE}.openai.azure.com",
            api_version=AZURE_OPENAI_API_VERSION,
            api_key = AZURE_OPENAI_TOKEN
        )
    
    def chat_completions_create(
            self, system_message: str, user_message: str, 
            temperature = 0.0, max_tokens = 4096
        ) -> str:
        messages = self._create_messages(system_message, user_message)
        response = self.__openai_client.chat.completions.create(
            model = self.__AZURE_OPENAI_DEPLOYMENT,
            messages = messages,
            temperature = temperature,
            max_tokens = max_tokens,
            n=1
        )
        return response.choices[0].message.content

    def _create_messages(self, system_message: str, user_message: str) -> list[dict]:
        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
