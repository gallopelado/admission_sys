import os
from flask import Flask, request, jsonify
import jwt
from functools import wraps

app = Flask(__name__)

# Definimos rutas estáticas
app.config['APPLICATION_PROPERTIES'] = os.path.join(os.path.abspath(os.getcwd()), 'src/resources/application.properties.yaml')

# Trabajar el JWT
app.config['SECRET_KEY'] = 'miclavesecreta'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            from src.main.models.seguridad.login.dao.LoginDao import LoginDao
            u = LoginDao()
            ## traer el usuario y su rol para validar privilegios, luego retornarlo en la funcion f(current_user, *args, **kwargs)
            current_user = u.getUsuarioByCodigoUsuario(data['codigo_usuario'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

# Modulos de referenciales
from src.main.rutas.referenciales.ciudad.ciudad_routes import ciudadMod

# Modulos de seguridad
from src.main.rutas.seguridad.login.login_routes import loginMod

#Modulos de admision
from src.main.rutas.admision.admision_routes import admisionMod

#Modulos de preconsulta
from src.main.rutas.preconsulta.preconsulta_routes import preconsultaMod

#Modulos de consulta
from src.main.rutas.consulta.consulta_routes import consultaMod

# Raiz
api = "/apiv1"

# Registrar modulos de referenciales
modulo0 = f"{api}/referenciales"
app.register_blueprint(ciudadMod, url_prefix=f"{modulo0}/ciudad")

# Registrar modulos de seguridad
modulo1 = f"{api}/seguridad"
app.register_blueprint(loginMod, url_prefix=f"{modulo1}/login")

# Registrar modulos de admision
modulo2 = f"{api}/admision"
app.register_blueprint(admisionMod, url_prefix=f"{modulo2}")

# Registrar modulos de preconsulta
modulo3 = f"{api}/preconsulta"
app.register_blueprint(preconsultaMod, url_prefix=f"{modulo3}")

# Registrar modulos de consulta
modulo3 = f"{api}/consulta"
app.register_blueprint(consultaMod, url_prefix=f"{modulo3}")

@app.route('/')
def method_name():
    return "Hola Mundo"