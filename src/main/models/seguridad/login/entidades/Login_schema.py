from dataclasses import field
from marshmallow import Schema, fields

class Login_schema(Schema):
    usuCodigoUsuario = fields.Str()
    usuPassword = fields.Str()
    usuNombres = fields.Str()
    usuApellidos = fields.Str()
    usuDescripcion = fields.Str()
    usuEstado = fields.Str()
    usuRol = fields.Str()
    usuCreacion_usuario = fields.Str()
    usuCreacion_fecha = fields.Date()
    usuCreacion_hora = fields.Time()
    usuModificacion_usuario = fields.Str()
    usuModificacion_fecha = fields.Date()
    usuModificacion_hora = fields.Time()
    operacion = fields.Str()