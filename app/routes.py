from flask import Blueprint, request, jsonify
from app.gemini_api import get_suggested_title
import random
from datetime import datetime

# Crear un blueprint llamado api_bp
# Este blueprint manejará todas las rutas relacionadas con la API
api_bp = Blueprint('api', __name__)

# Definir una ruta para agregar una tarea
@api_bp.route('/task', methods=['POST'])
def add_task():
    # Obtener los datos de la tarea del cuerpo de la solicitud
    task_data = request.json
    items = task_data.get('items')
    
    # Verificar si se proporcionó un estado válido
    if not task_data.get('status') == 'new':
        return jsonify({"error": "Invalid status"}), 400
    
    # Verificar si se proporcionaron los datos de los elementos
    if not items:
        return jsonify({"error": "No items data provided"}), 400
    
    # Obtener títulos sugeridos para la tarea    
    suggested_titles = get_suggested_title(items)
    
    print("Titulos sugeridos", suggested_titles)

    # Seleccionar un título aleatorio de la lista de títulos sugeridos
    title = suggested_titles[random.randint(0, 4)]['title']
    
    # Modificar los datos de la tarea con el título sugerido y otros detalles
    task_data['title'] = title
    task_data['status'] = 'pending'
    task_data['created_at'] = datetime.now()
    task_data['updated_at'] = datetime.now()

    # Devolver los datos de la tarea modificada con el código de estado 201 (creado)
    return jsonify(task_data), 201
