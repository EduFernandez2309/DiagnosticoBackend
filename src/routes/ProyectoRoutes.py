from flask import Blueprint, jsonify, request
from src.models.ProyectoModel import ProyectoModel 

main=Blueprint('pr_blueprint', __name__)

@main.route('')
def get_proyectos():
    try:
        proyectos = ProyectoModel.get_proyectos()
        if len(proyectos) > 0:
            return  jsonify({'proyecto': proyectos, 'message': 'SUCCESS'})
        else:
            return jsonify({'message':'NOTFOUND', 'success':True})
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('', methods=['POST'])
def insert_proyecto():
    try:
        data = request.json
        proyecto = ProyectoModel.insert_proyecto(data)
        return jsonify({'proyecto':proyecto, 'message': 'Proyecto insertado exitosamente', 'success': True})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<int:proyecto_id>', methods=['PUT'])
def update_proyecto(proyecto_id):
    try:
        data = request.json

        ProyectoModel.update_proyecto(proyecto_id, data)
        return jsonify({'message': f'Proyecto con ID {proyecto_id} actualizado exitosamente', 'success': True}), 201
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<int:proyecto_id>', methods=['DELETE'])
def delete_proyecto(proyecto_id):
    try:
        ProyectoModel.delete_proyecto(proyecto_id)
        return jsonify({'message': f'Proyecto con ID {proyecto_id} eliminado exitosamente', 'success': True})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500