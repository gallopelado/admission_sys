from hashlib import sha256
from datetime import date, datetime, timedelta
from flask import Blueprint, jsonify, request, make_response, current_app as app
import jwt
from werkzeug.security import check_password_hash, generate_password_hash
from src.main import token_required
from src.main.models.seguridad.login.dao.LoginDao import LoginDao
from src.main.models.seguridad.login.entidades.Logindto import Logindto
from src.main.models.seguridad.login.entidades.Login_schema import Login_schema

# Modularizar
loginMod = Blueprint("loginMod", __name__)
logindao = LoginDao()
fecha_actual_server = date.today()
hora_actual_server = datetime.now().strftime("%H:%M:%S")

@loginMod.route("/")
def login():
    auth = request.authorization
    
    if not auth or not auth.username or not auth.password:
        return make_response('No se pudo verificar', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    user = logindao.getUsuarioByCodigoUsuario(auth.username)
    
    if not user:
        return make_response('No se pudo verificar', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    if check_password_hash(user.usuPassword, auth.password):
        token = jwt.encode({'codigo_usuario' : user.usuCodigoUsuario, 'exp' : datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    
    return make_response('No se pudo verificar', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@loginMod.route("/get_usuarios")
@token_required
def getUsuarios(current_user):
    items = logindao.listarTodos()
    schema = Login_schema(many=True)
    if items:
        return jsonify(schema.dump(items)), 200
    else:
        return jsonify("{'estado':'correcto', 'mensaje':'No existen usuario'}"), 200

@loginMod.route("/get_usuario_by_codigo_usuario/<string:codigousuario>")
@token_required
def getUsuariosByCodigoUsuario(current_user, codigousuario):
    item = logindao.getUsuarioByCodigoUsuario(codigousuario)
    schema = Login_schema()
    if item:
        return jsonify(schema.dump(item)), 200
    else:
        return jsonify("{'estado':'correcto', 'mensaje':'No existe usuario'}"), 200

@loginMod.route("/add_usuario", methods=["POST"])
@token_required
def addUsuario(current_user):
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
@token_required
def modifyUsuario(current_user):
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
@token_required
def deleteUsuario(current_user, codigousuario):
    resp = logindao.eliminar(codigousuario)
    if resp==True:
        return jsonify("{'estado':'correcto', 'mensaje':'Se ha eliminado'}"), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha eliminado'}")

@loginMod.route("/check_user_password", methods=["POST"])
@token_required
def checkUserAndPassword(current_user):
    json = request.get_json()
    ## Trabajar el password a sha256
    password = json['password']
    ##passwordHashed = sha256(password.encode('utf8')).hexdigest()
    usuario = logindao.getUserAndPassword(json['codigo_usuario'], password)
    schema = Login_schema()
    if usuario:
        return jsonify(schema.dump(usuario)), 200
    return jsonify("{'estado':'error', 'mensaje':'No se ha encontrado el usuario'}"), 404