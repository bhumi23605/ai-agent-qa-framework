from google import genai
import os
class SimpleAgent:
    """
    LLM powered agent used by QA evaluation framework. 
    """

    def __init__(self):
        self.client=genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    def ask(self,question:str)->str:
        response=self.client.models.generate_content(model="gemini-3.6-flash",contents=question)
        return response.text
    