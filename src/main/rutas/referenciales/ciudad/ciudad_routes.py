from flask import Blueprint, jsonify, request
from src.main.models.referenciales.ciudad.CiudadDao import CiudadDao

# Modularizar
ciudadMod = Blueprint("ciudadMod", __name__)
cdao = CiudadDao()

@ciudadMod.route("/get_ciudades")
def getCiudades():
    items = cdao.listarTodos()
    return jsonify(items), 200

@ciudadMod.route("/get_ciudad_by_id/<int:idciudad>")
def getCiudadById(idciudad):
    item = cdao.getById(idciudad)
    return jsonify(item), 200

@ciudadMod.route("/add_ciudad", methods=["POST"])
def addCiudad():
    json = request.get_json()
    resp = cdao.agregar(json['ciu_descripcion'])
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha agregado'}"), 201
    return jsonify("{'estado':'error', 'mensaje':'No se ha agregado'}"), 500

@ciudadMod.route("/modify_ciudad", methods=["PUT"])
def modifyCiudad():
    json = request.get_json()
    transaction_key = ['ciu_id', 'ciu_descripcion']
    if not all(key in json for key in transaction_key):
        return 'Faltan algunos elementos de la transacción', 400
    resp = cdao.modificar(json['ciu_id'], json['ciu_descripcion'])
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha modificado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha modificado'}")

@ciudadMod.route("/delete_ciudad/<int:idciudad>", methods=['DELETE'])
def deleteCiudad(idciudad):
    resp = cdao.eliminar(idciudad)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha eliminado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha eliminado'}")
