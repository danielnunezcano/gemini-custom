import unittest
from unittest.mock import patch, MagicMock, mock_open
from custom_gemini.generative_model import generate_response
from custom_gemini.generative_model import generate_image_response
from custom_gemini.generative_model import generate_audio_response


class TestGenerativeModelFunctions(unittest.TestCase):

    @patch("custom_gemini.generative_model.model")
    def test_generate_response(self, mock_model):
        # Mock de la respuesta del modelo
        mock_response = MagicMock()
        mock_response.text = "Hola, esto es una respuesta limpia.```"
        mock_model.generate_content.return_value = mock_response

        # Ejecutar la función con parámetros de prueba
        question = "¿Cuál es la capital de"
        value = "Francia?"
        result = generate_response(question, value)

        # Verificar el resultado esperado
        self.assertEqual(result, "Hola, esto es una respuesta limpia.")
        mock_model.generate_content.assert_called_once_with("¿Cuál es la capital de Francia?")

    @patch("custom_gemini.generative_model.model")
    @patch("builtins.open", new_callable=mock_open, read_data=b"fake_image_data")
    def test_generate_image_response(self, mock_open, mock_model):
        # Mock de la respuesta del modelo
        mock_response = MagicMock()
        mock_response.text = "Resumen generado para las imágenes."
        mock_model.generate_content.return_value = mock_response

        # Configuración de prueba
        prompt = "Describe estas imágenes:"
        images = ["/path/to/image1.jpg", "/path/to/image2.jpg"]

        result = generate_image_response(prompt, images)

        # Verificar el resultado esperado
        self.assertEqual(result, "Resumen generado para las imágenes.")
        mock_open.assert_called_with("/path/to/image2.jpg", "rb")  # Última imagen abierta
        mock_model.generate_content.assert_called_once()
        self.assertIn("mime_type", mock_model.generate_content.call_args[0][0][0])  # Comprobando el formato

    @patch("custom_gemini.generative_model.model")
    @patch("custom_gemini.generative_model.genai.upload_file")
    def test_generate_audio_response(self, mock_upload_file, mock_model):
        # Mock del archivo subido y la respuesta del modelo
        mock_upload_file.return_value = "uploaded_file_reference"
        mock_response = MagicMock()
        mock_response.text = "Resumen generado para el audio."
        mock_model.generate_content.return_value = mock_response

        # Configuración de prueba
        prompt = "Resume este audio:"
        audio_path = "/path/to/audio.mp3"

        result = generate_audio_response(prompt, audio_path)

        # Verificar el resultado esperado
        self.assertEqual(result, "Resumen generado para el audio.")
        mock_upload_file.assert_called_once_with(audio_path)
        mock_model.generate_content.assert_called_once_with(["uploaded_file_reference", prompt])

    @patch("custom_gemini.generative_model.model")
    @patch("builtins.open", new_callable=mock_open, read_data=b"fake_pdf_data")
    def test_generate_pdf_response(self, mock_open, mock_model):
        # Mock de la respuesta del modelo
        mock_response = MagicMock()
        mock_response.text = "Resumen generado para los pdf."
        mock_model.generate_content.return_value = mock_response

        # Configuración de prueba
        prompt = "Describe estos pdfs:"
        pdfs = ["/path/to/image1.pdf", "/path/to/image2.pdf"]

        result = generate_pdf_response(prompt, pdfs)

        # Verificar el resultado esperado
        self.assertEqual(result, "Resumen generado para los pdf.")
        mock_open.assert_called_with("/path/to/image2.pdf", "rb")  # Última imagen abierta
        mock_model.generate_content.assert_called_once()
        self.assertIn("mime_type", mock_model.generate_content.call_args[0][0][0])  # Comprobando el formato


if __name__ == "__main__":
    unittest.main()
