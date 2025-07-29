import os
from dotenv import load_dotenv
import google.generativeai as genai


class Intent_Detection :
    def __init__(self):
      load_dotenv()  # Load environment variables from .env
      self.api_key = os.getenv("GEMINI_API_KEY") # get the value inside GEMINI_API_KEY, note: the api is not actually hidden,i only did that to show how important it is to hide critical info
      if not self.api_key:
          raise ValueError("GEMINI_API_KEY not found in environment variables.")
        
      genai.configure(api_key=self.api_key)
      self.model = genai.GenerativeModel("gemini-2.5-pro")

    def detect_intent(self,user_input) : 


    def LLM_query(self,prompt) 
      response = self.model.generate_content(prompt)
      return response.text


class main() : 
  while True : 
    user_input = input("you : ")
    if intent : # functionality in detect_intent method


    else : # resort to llm
      respose = intent_detector.LLM_query(user_input) 
      print(f"LLM : {respose}) 
    
      


    

