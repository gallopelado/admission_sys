import os
from flask import Flask

app = Flask(__name__)

# Definimos rutas estáticas
app.config['APPLICATION_PROPERTIES'] = os.path.join(os.path.abspath(os.getcwd()), 'src/resources/application.properties.yaml')

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