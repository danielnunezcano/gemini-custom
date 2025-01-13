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
    return model.generate_content(prompt)


def generate_image_response(prompt, images):
    image_content = [prompt]
    for image_path in images:
        try:
            with open(image_path, "rb") as image_file:
                # Leer los datos de la imagen en memoria
                image_data = image_file.read()

                # Abrir la imagen con Pillow para obtener el formato
                img = Image.open(io.BytesIO(image_data))
                image_type = img.format.lower()

                if image_type in ALLOWED_MIME_TYPES:
                    image_content.append(img)  # Agregar la imagen de Pillow
                else:
                    print(f"Error: Formato de imagen no soportado {image_path}")
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado {image_path}")
            continue
        except UnidentifiedImageError:
            print(f"Error: No se pudo abrir o leer la imagen {image_path}")
            continue

    return model.generate_content(image_content).text

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