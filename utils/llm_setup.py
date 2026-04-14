import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class GroqLLMWrapper:
    def __init__(self, model: str, api_key: str | None):
        self.client = ChatGroq(model=model, api_key=api_key)

    def call(self, prompt: str) -> str:
        response = self.client.invoke(prompt)
        return getattr(response, "content", str(response))


def get_llm():
    return GroqLLMWrapper(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
    )