import google.generativeai as genai
from google.cloud import aiplatform
from PIL import Image, UnidentifiedImageError
import base64
import os
import re
from google.protobuf.json_format import MessageToJson

ALLOWED_MIME_TYPES = {
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "webp": "image/webp",
    "heic": "image/heic",
    "heif": "image/heif",
}

PROJECT_ID = "haltcatchyoutubeuploadpython"
LOCATION = "us-central1"

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

def crear_imagen_desde_json():
    """Lee un archivo JSON, extrae la imagen en Base64 y la guarda como PNG."""
    
    # 1️⃣ Leer el JSON desde el archivo
    with open("image.txt", "r", encoding="utf-8") as f:
        data = f.read()

    try:
        mime_type = "image/png"

        # 3️⃣ Decodificar Base64 a bytes
        imagen_bytes = base64.b64decode(data)

        # 4️⃣ Guardar la imagen en un archivo
        with open("image.png", "wb") as img_file:
            img_file.write(imagen_bytes)

        print(f"✅ Imagen guardada como {"image.png"} ({mime_type})")

    except KeyError as e:
        print(f"❌ Error: No se encontró la clave {e} en el JSON.")
        
def generate_image(prompt,image_name):
    generate_image_vertex(prompt)
    extraer_imagen_desde_texto("response_vertex_ai.txt", image_name)
            
def generate_image_vertex(prompt):
    """Genera una imagen con Google Cloud Vertex AI y muestra el contenido completo de response."""
    client = aiplatform.gapic.PredictionServiceClient()

    # Definir el endpoint correcto
    endpoint = f"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/imagegeneration@002"

    # Construir la solicitud
    instance = {"prompt": prompt}
    response = client.predict(endpoint=endpoint, instances=[instance])

    # 🔹 Guardar response en un archivo de texto
    with open("response_vertex_ai.txt", "w", encoding="utf-8") as f:
        f.write(str(response))
    

def extraer_imagen_desde_texto(nombre_archivo_txt, nombre_imagen):
    """Lee un archivo de texto plano, extrae la imagen Base64 y la guarda como PNG."""

    with open(nombre_archivo_txt, "r", encoding="utf-8") as f:
        contenido = f.read()  # Leer todo el contenido del archivo de texto

    # Expresión regular mejorada para encontrar 'bytesBase64Encoded' y su contenido en string_value
    match = re.search(r'key:\s*"bytesBase64Encoded"\s*value\s*\{\s*string_value:\s*"([^"]+)"', contenido)

    if match:
        imagen_base64 = match.group(1)  # Extraer la parte Base64 de la respuesta

        # Decodificar Base64 a bytes
        imagen_bytes = base64.b64decode(imagen_base64)

        # Guardar la imagen en un archivo
        with open(nombre_imagen, "wb") as img_file:
            img_file.write(imagen_bytes)

        print(f"✅ Imagen guardada como {nombre_imagen}")
    else:
        print("❌ No se encontró la clave 'bytesBase64Encoded' en el archivo.")






