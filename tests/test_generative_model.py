import unittest
from unittest.mock import patch, MagicMock
from custom_gemini.generative_model import generate_clean_response

class TestGenerateCleanResponse(unittest.TestCase):

    @patch("custom_gemini.generative_model.model")
    def test_generate_clean_response(self, mock_model):
        # Configurar el mock para simular la respuesta del modelo
        mock_response = MagicMock()
        mock_response.text = "Hola, esto es una respuesta limpia.```"
        mock_model.generate_content.return_value = mock_response

        # Llamar a la función con parámetros de prueba
        question = "¿Cuál es la capital de"
        value = "Francia?"
        result = generate_clean_response(question, value)

        # Verificar el resultado esperado
        self.assertEqual(result, "Hola, esto es una respuesta limpia.")

        # Verificar que se llamó a `generate_content` con el input correcto
        mock_model.generate_content.assert_called_once_with("¿Cuál es la capital de Francia?")

if __name__ == "__main__":
    unittest.main()
