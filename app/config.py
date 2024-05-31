import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')