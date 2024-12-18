import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(os.environ["GEMINI_MODEL"])

def generate_clean_response(question_to_gemini,value):
    response = model.generate_content(question_to_gemini+" "+value)
    return response.text.rstrip().replace("```","").replace(f"\n","")