from flask import Blueprint, jsonify, request
from src.models.TipoProyectoModel import TipoProyectoModel 

main = Blueprint('tipo_proyecto_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_tipos_proyecto():
    try:
        tipos_proyecto = TipoProyectoModel.get_tipos_proyecto()
        if len(tipos_proyecto) > 0:
            return jsonify({'tipos_proyecto': tipos_proyecto, 'message': 'SUCCESS'})
        else:
            return jsonify({'message':'NOTFOUND', 'success':True})
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/', methods=['POST', 'OPTIONS'])
def insert_tipo_proyecto():
    try:
        data = request.json
        tipo_proyecto = TipoProyectoModel.insert_tipo_proyecto(data)
        return jsonify({'tipo_proyecto': tipo_proyecto, 'message': 'Tipo de proyecto insertado exitosamente', 'success': True}), 201
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<int:tipo_proyecto_id>', methods=['PUT'])
def update_tipo_proyecto(tipo_proyecto_id):
    try:
        data = request.json

        TipoProyectoModel.update_tipo_proyecto(tipo_proyecto_id, data)
        return jsonify({'message': f'Tipo de proyecto con ID {tipo_proyecto_id} actualizado exitosamente', 'success': True}), 201
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<int:tipo_proyecto_id>', methods=['DELETE'])
def delete_tipo_proyecto(tipo_proyecto_id):
    try:
        TipoProyectoModel.delete_tipo_proyecto(tipo_proyecto_id)
        return jsonify({'message': f'Tipo de proyecto con ID {tipo_proyecto_id} eliminado exitosamente', 'success': True})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
