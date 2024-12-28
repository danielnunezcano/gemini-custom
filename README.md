# Librería de Generación de Respuestas Multimodales con Google Gemini API

Esta librería permite generar respuestas utilizando el modelo de lenguaje Gemini de Google a través de su API, soportando texto, imágenes, audio y PDFs.

## Requisitos Previos

Para utilizar esta librería, asegúrate de tener lo siguiente configurado:

1. **Clave de API de Google Gemini**.
2. **Nombre del modelo Gemini** (por ejemplo, `gemini-pro`).

Configura las siguientes variables de entorno:

```bash
export GEMINI_API_KEY="tu_clave_api"
export GEMINI_MODEL="gemini-pro"
```

## Instalación

*Nota: La estructura del proyecto y los pasos de instalación asumen una estructura similar al ejemplo. Adapta estos pasos según la organización real de tu proyecto.*

1. **Clonar el repositorio (si aplica):**

    ```bash
    git clone https://github.com/danielnunezcano/gemini-custom.git
    cd <nombre_de_tu_repositorio>
    ```
2. **Instalar la librería (si aplica):**

    ```bash
    pip install .
    ```
3. **Instalar las dependencias:**

    ```bash
    pip install google-generativeai
    ```

## Uso

### Ejemplo de código

#### Generación de respuesta a partir de texto:

```python
from custom_gemini.generative_model import generate_response

prompt = "¿Cuál es la capital de Francia?"

response = generate_response(prompt)
print(response)  # Salida esperada: "París"
```

#### Generación de respuesta a partir de imágenes:

```python
from custom_gemini.generative_model import generate_image_response

prompt = "¿Qué hay en estas imágenes?"
image_paths = ["imagen1.jpg", "imagen2.png"]  # Asegúrate de que los archivos existan

response = generate_image_response(prompt, image_paths)
print(response)
```

#### Generación de respuesta a partir de audio:

```python
from custom_gemini.generative_model import generate_audio_response

prompt = "Describe el contenido del audio."
audio_path = "audio.mp3"  # Asegúrate de que el archivo exista

response = generate_audio_response(prompt, audio_path)
print(response)
```

#### Generación de respuesta a partir de pdfs:

```python
from custom_gemini.generative_model import generate_image_response

prompt = "¿Qué hay en estos pdfs?"
pdf_paths = ["file1.pdf", "file2.pdf"]  # Asegúrate de que los archivos existan

response = generate_pdf_response(prompt, pdf_paths)
print(response)
```

## Descripción de las Funciones

### `generate_response(prompt, value)`

-   **Descripción**: Envía un prompt de texto al modelo Gemini y devuelve una respuesta limpia sin caracteres no deseados.
-   **Parámetros**:
  -   `prompt` (str): El prompt que quieres enviar.
-   **Retorno**: Respuesta en formato texto limpio.

### `generate_image_response(prompt, images)`

-   **Descripción**: Envía un prompt y una lista de imágenes al modelo Gemini y devuelve una respuesta de texto.
-   **Parámetros**:
  -   `prompt` (str): El prompt relacionado con las imágenes.
  -   `images` (list): Una lista de rutas a los archivos de imagen.
-   **Retorno**: Respuesta en formato texto.
-   **Formatos de Imagen Soportados**:
  -   **PNG** - `image/png`
  -   **JPEG** - `image/jpeg`
  -   **WEBP** - `image/webp`
  -   **HEIC** - `image/heic`
  -   **HEIF** - `image/heif`

### `generate_audio_response(prompt, audio)`

-   **Descripción**: Envía un prompt y un archivo de audio al modelo Gemini y devuelve una respuesta de texto.
-   **Parámetros**:
  -   `prompt` (str): El prompt relacionado con el audio.
  -   `audio` (str): La ruta al archivo de audio.
-   **Retorno**: Respuesta en formato texto.
-   **Formatos de Audio Soportados**:
  -   **WAV** - `audio/wav`
  -   **MP3** - `audio/mp3`
  -   **AIFF** - `audio/aiff`
  -   **AAC** - `audio/aac`
  -   **OGG Vorbis** - `audio/ogg`
  -   **FLAC** - `audio/flac`

### `generate_pdf_response(prompt, images)`

-   **Descripción**: Envía un prompt y una lista de PDFs al modelo Gemini y devuelve una respuesta de texto.
-   **Parámetros**:
  -   `prompt` (str): El prompt relacionado con las imágenes.
  -   `pdfs` (list): Una lista de rutas a los archivos de pdf.
-   **Retorno**: Respuesta en formato texto.

## Estructura del Proyecto (Ejemplo)

```
custom_gemini/
│
├── custom_gemini/
│   ├── __init__.py
│   └── generative_model.py
│
├── setup.py
└── README.md
```

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

**Daniel Núñez Cano**
[Github](https://github.com/danielnunezcano)
