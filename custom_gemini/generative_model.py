import google.generativeai as genai
from PIL import Image, UnidentifiedImageError
import base64
import os
import io

ALLOWED_MIME_TYPES = {
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "webp": "image/webp",
    "heic": "image/heic",
    "heif": "image/heif",
}

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(os.environ["GEMINI_MODEL"])

def generate_response(prompt):
    return model.generate_content(prompt).text

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
    return model.generate_content(image_content).text

def generate_audio_response(prompt, audio):
    myfile = genai.upload_file(audio)
    return model.generate_content([myfile, prompt]).text

def generate_pdf_response(prompt, file):
    with open(file, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")
    response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])
    return response.text