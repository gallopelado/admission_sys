from crypt import methods
from flask import Blueprint, jsonify, request
from src.main.models.preconsulta.Preconsultadao import PreconsultaDao
from src.main.models.preconsulta.Preconsultadto import PreconsultaDto

# Modularizar
preconsultaMod = Blueprint("preconsultaMod", __name__)
precdao = PreconsultaDao()

@preconsultaMod.route("/get_preconsulta_by_codigo_establecimiento_and_codigo_asignacion/<codigo_establecimiento>/<codigo_asignacion>", methods=['GET'])
def getPreconsultaByCodigoEstablecimientoAndCodigoAsignacion(codigo_establecimiento, codigo_asignacion):
    items = precdao.getPreconsultaData(codigo_establecimiento, codigo_asignacion)
    return jsonify(items), 200

@preconsultaMod.route("/update_preconsulta", methods=['PUT'])
def updatePreconsulta():
    json = request.get_json()
    pre = PreconsultaDto(json['precon_codigo_establecimiento'], json['pacasi_codigo_asignacion'], json['precon_creacion_fecha']
                 , json['precon_temperatura_corporal'], json['precon_presion_arterial'], json['precon_frecuencia_respiratoria']
                 , json['precon_pulso'], json['precon_peso'], json['precon_talla'], json['precon_imc'], json['precon_saturacion']
                 , json['precon_circunferencia_abdominal'], json['precon_motivo_consulta'], json['precon_creacion_usuario'])
    items = precdao.updatePreconsultaData(pre)
    if items and items.precon_modificacion_fecha != '':
        return jsonify({'estado':'correcto', 'mensaje':'Se ha realizado'}), 200
    else:
        return jsonify({'estado':'error', 'mensaje':'No se ha realizado'}), 500