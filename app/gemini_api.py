from flask import current_app
import json
import google.generativeai as genai

def get_suggested_title(items):
    GEMINI_API_KEY = current_app.config['GEMINI_API_KEY']
    # Inicializar la configuración de la API de Gemini
    genai.configure(api_key=GEMINI_API_KEY)
    # Crear una instancia del modelo generativo con la configuración de generación específica
    # response_mime_type: application/json (para obtener una respuesta en formato JSON)
    # temperature: 0.7 (para controlar la variabilidad de las respuestas generadas)
    model = genai.GenerativeModel('gemini-1.5-flash', 
        generation_config={
            "response_mime_type": "application/json",
            "temperature": 0.5,
            }
        )
    # Crear el prompt para la generación de títulos sugeridos
    prompt = f"List 5 non-specific suggestions for a task title that includes the following elements: {items}."

    # Generar títulos sugeridos en formato JSON
    format_prompt = prompt + """
    
    The suggested titles should be in the language in which the elements are written.

    Using this JSON schema:

    Title = {"title": str}

    Return a `list[Title]`
    """

    # Generar contenido con el modelo generativo
    response = model.generate_content(format_prompt)
    # response = "[{"title": "suggested title 1"},...]"
    # loads <- convierte un string en un diccionario
    data = json.loads(response.text)
    
    return data
