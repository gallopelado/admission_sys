from marshmallow import Schema, fields

class Ciudad_schema(Schema):
    ciuId = fields.Int()
    ciuDescripcion = fields.Str()