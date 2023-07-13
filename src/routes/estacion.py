from flask import Blueprint, jsonify

main=Blueprint('estacion_blueprint',__name__)

@main.route('/')
def get_estacion():
    return jsonify({'message':"JORGE"})