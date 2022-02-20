from hashlib import sha256
from datetime import date, datetime
from flask import Blueprint, jsonify, request
from src.main.models.seguridad.login.dao.LoginDao import LoginDao
from src.main.models.seguridad.login.entidades.Logindto import Logindto
from src.main.models.seguridad.login.entidades.Login_schema import Login_schema

# Modularizar
loginMod = Blueprint("loginMod", __name__)
logindao = LoginDao()

@loginMod.route("/get_usuarios")
def getUsuarios():
    items = logindao.listarTodos()
    schema = Login_schema(many=True)
    if items:
        return jsonify(schema.dump(items)), 200
    else:
        return jsonify("{'estado':'correcto', 'mensaje':'No existen usuario'}"), 200

@loginMod.route("/get_usuario_by_codigo_usuario/<string:codigousuario>")
def getUsuariosByCodigoUsuario(codigousuario):
    item = logindao.getUsuarioByCodigoUsuario(codigousuario)
    schema = Login_schema()
    if item:
        return jsonify(schema.dump(item)), 200
    else:
        return jsonify("{'estado':'correcto', 'mensaje':'No existe usuario'}"), 200

@loginMod.route("/add_usuario", methods=["POST"])
def addUsuario():
    json = request.get_json()
    ## Trabajar el password a sha256
    password = json['password']
    passwordHashed = sha256(password.encode('utf8')).hexdigest()
    # Cargar datos al dto
    now = datetime.now()
    usuario = Logindto(json['codigo_usuario'], passwordHashed, json['nombres'], json['apellidos'], json['descripcion'], json['estado'], json['rol'], json['creacion_usuario'], date.today(), now.strftime("%H:%M:%S"))
    resp = logindao.agregarUsuario(usuario)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha agregado'}"), 201
    return jsonify("{'estado':'error', 'mensaje':'No se ha agregado'}"), 500

@loginMod.route("/modify_usuario", methods=["PUT"])
def modifyUsuario():
    json = request.get_json()
    transaction_key = ['codigo_usuario', 'password', 'nombres', 'apellidos', 'descripcion', 'estado', 'rol', 'creacion_usuario']
    if not all(key in json for key in transaction_key):
        return 'Faltan algunos elementos de la transacción', 400
    ## Trabajar el password a sha256
    password = json['password']
    passwordHashed = sha256(password.encode('utf8')).hexdigest()
    # Cargar datos al dto
    now = datetime.now()
    usuario = Logindto(json['codigo_usuario'], passwordHashed, json['nombres'], json['apellidos'], json['descripcion'], json['estado'], json['rol'], None, None, None, json['creacion_usuario'], date.today(), now.strftime("%H:%M:%S"))
    resp = logindao.modificarUsuario(usuario)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha modificado'}"), 201
    return jsonify("{'estado':'error', 'mensaje':'No se ha modificado'}"), 500

@loginMod.route("/delete_usuario/<string:codigousuario>", methods=['DELETE'])
def deleteUsuario(codigousuario):
    resp = logindao.eliminar(codigousuario)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha eliminado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha eliminado'}")