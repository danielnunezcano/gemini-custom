import google.generativeai as genai
import base64
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(os.environ["GEMINI_MODEL"])

def generate_clean_response(prompt):
    return model.generate_content(prompt)

def generate_clean_image_response(prompt, images):
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

    response = model.generate_content(image_content)

    return response.text

def generate_clean_audio_response(prompt, audio):
    myfile = genai.upload_file(audio)
    result = model.generate_content([myfile, prompt])
    return result.text

