
class Logindto:
    def __init__(self, codigo_usuario="", password="", nombres="", apellidos="", descripcion="", estado="", rol="", creacion_usuario="", creacion_fecha=None, creacion_hora=None, modificacion_usuario="", modificacion_fecha=None, modificacion_hora=None, operacion=""):
        self.usuCodigoUsuario = codigo_usuario
        self.usuPassword = password
        self.usuNombres = nombres.upper()
        self.usuApellidos = apellidos.upper()
        self.usuDescripcion = descripcion
        self.usuEstado = estado
        self.usuRol = rol
        self.usuCreacion_usuario = creacion_usuario
        self.usuCreacion_fecha = creacion_fecha
        self.usuCreacion_hora = creacion_hora
        self.usuModificacion_usuario = modificacion_usuario
        self.usuModificacion_fecha = modificacion_fecha
        self.usuModificacion_hora = modificacion_hora
        self.operacion = operacion