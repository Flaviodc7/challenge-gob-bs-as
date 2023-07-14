from flask import Blueprint, jsonify, request

from src.models.entities.EstacionEdit import EstacionEdit

from src.models.entities.EstacionAdd import EstacionAdd

from src.models.EstacionModelo import EstacionModelo

main=Blueprint('estacion_blueprint',__name__)

@main.route('/')
def get_estaciones():
    try:
        estaciones = EstacionModelo.get_estaciones()
        return jsonify(estaciones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/<id>')
def get_estacion(id):
    try:
        estacion = EstacionModelo.get_estacion(id)
        if estacion != None:
            return jsonify(estacion)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/', methods = ['POST'])
def add_estacion():
    try:
        name = request.json['name']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        estacion = EstacionAdd(name, latitude, longitude)

        affected_rows = EstacionModelo.add_estacion(estacion)

        if affected_rows == 1:
            return jsonify(estacion.name)

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods = ['DELETE'])
def delete_estacion(id):
    try:
        affected_rows = EstacionModelo.delete_estacion(id)

        if affected_rows == 1:
            return jsonify(id)

    except Exception as ex:
        return jsonify({'message': "Can't find station to delete"}), 404

@main.route('/update/', methods = ['PUT'])
def update_estacion():
    try:
        id = request.json['id']
        name = request.json['name']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        estacion = EstacionEdit(id, name, latitude, longitude)

        affected_rows = EstacionModelo.update_estacion(estacion)

        if affected_rows == 1:
            return jsonify(estacion.name)

    except Exception as ex:
        return jsonify({'message': "No station found"}), 500