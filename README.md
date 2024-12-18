# Librería de Generación de Respuestas con Google Gemini API

Esta librería permite generar respuestas limpias utilizando el modelo de lenguaje Gemini de Google a través de su API.

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
1. **Clonar el repositorio:**
```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

2. **Instalar la librería:**
```bash
pip install .
```

3. **Instalar la dependencia google-generativeai (si no se instala automáticamente):**
```bash
pip install google-generativeai
```

## Uso
### Ejemplo de código
```python
from mi_libreria.generative_model import generate_clean_response

# Pregunta y valor a enviar al modelo
pregunta = "¿Cuál es la capital de"
valor = "Francia?"

# Generar respuesta limpia
respuesta = generate_clean_response(pregunta, valor)
print(respuesta)  # Salida esperada: "París"
```

## Descripción de la Función
`generate_clean_response(question_to_gemini, value)`

- **Descripción**:
    Envía una pregunta al modelo Gemini y devuelve una respuesta limpia sin caracteres no deseados.
- **Parámetros**:
  - `question_to_gemini` (str): La pregunta que quieres hacer.
  - `value` (str): Información adicional para completar la pregunta.
- Retorno:
- Respuesta en formato texto limpio.

## Estructura del Proyecto
```arduino
mi_libreria/
│
├── mi_libreria/
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

