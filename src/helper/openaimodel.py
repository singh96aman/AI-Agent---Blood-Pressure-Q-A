from constants import Constants
from openai import OpenAI
import os

class OpenAIModel:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_KEY'))
        self.model = Constants.GPT_MODEL

    def predict(self, prompt):
        messages = [{'role': 'user', 'content': prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages).choices[0].message.content
        return response