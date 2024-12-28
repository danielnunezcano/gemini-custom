import google.generativeai as genai
import base64
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(os.environ["GEMINI_MODEL"])

def generate_response(prompt):
    return model.generate_content(prompt)

def generate_image_response(prompt, images):
    image_content = []
    for image_path in images:
        try:
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                image_content.append({
                    'mime_type': 'image/jpeg',
                    'data': base64.b64encode(image_data).decode('utf-8')
                })
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado {image_path}")
            continue
    image_content.append(prompt)
    return model.generate_content(image_content)

def generate_audio_response(prompt, audio):
    myfile = genai.upload_file(audio)
    return model.generate_content([myfile, prompt])

def generate_pdf_response(prompt, files):
    docs_data = []
    for file in files:
        with open(file, "rb") as doc_file:
            doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")
            docs_data.append({'mime_type': 'application/pdf', 'data': doc_data})
    docs_data.append(prompt)
    return model.generate_content(docs_data)

