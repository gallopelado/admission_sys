from flask import Blueprint, jsonify, request
from src.main.models.consulta.Consultadao import ConsultaDao
from src.main.models.consulta.Consultadto import ConsultaDto
from src.main.models.consulta.ConsultaProcedimientosdto import ConsultaProcedimientosDto

# Modularizar
consultaMod = Blueprint("consultaMod", __name__)
consdao = ConsultaDao()

@consultaMod.route("/get_consulta_by_codigo_establecimiento_and_codigo_asignacion_and_creacion_fecha", methods=['GET'])
def getConsultaData():
    json = request.get_json()
    items = consdao.getConsultaData(json['codigo_establecimiento'], json['codigo_asignacion'], json['creacion_fecha'])
    return jsonify(items), 200

@consultaMod.route("/get_consulta_procedimientos_by_codigo_establecimiento_and_codigo_asignacion_and_creacion_fecha", methods=['GET'])
def getConsultaProcedimientosData():
    json = request.get_json()
    items = consdao.getConsultaProcedimientosData(json['codigo_establecimiento'], json['codigo_asignacion'], json['creacion_fecha'])
    return jsonify(items), 200

@consultaMod.route("/update_consulta", methods=['PUT'])
def updatePreconsulta():
    json = request.get_json()
    consulta = ConsultaDto(json['con_codigo_establecimiento'], json['pacasi_codigo_asignacion'], json['con_creacion_fecha']
                 , json['con_motivo_consulta'], json['con_historial_actual'], json['con_evolucion'], json['con_creacion_usuario'])
    items = consdao.updatePreconsultaData(consulta)
    if items and items.pacasi_codigo_asignacion != '':
        return jsonify({'estado':'correcto', 'mensaje':'Se ha realizado'}), 200
    else:
        return jsonify({'estado':'error', 'mensaje':'No se ha realizado'}), 500
    
@consultaMod.route("/update_consulta_procedimientos", methods=['PUT'])
def updatePreconsultaProcedimientosData():
    json = request.get_json()
    procedimientos = ConsultaProcedimientosDto(json['pacasi_codigo_asignacion'], json['con_codigo_establecimiento'], json['con_creacion_fecha'], json['cie_id'])
    items = consdao.updatePreconsultaProcedimientosData(procedimientos)
    if items and items.cie_id != '':
        return jsonify({'estado':'correcto', 'mensaje':'Se ha realizado'}), 200
    else:
        return jsonify({'estado':'error', 'mensaje':'No se ha realizado'}), 500
    
@consultaMod.route("/update_consulta_procedimientos_detalle", methods=['PUT'])
def updatePreconsultaProcedimientosDetalle():
    lista_procedimientos = []
    json = request.get_json()
    # recolectar los datos de la petición
    ## Consulta
    consulta = ConsultaDto(json['con_codigo_establecimiento'], json['pacasi_codigo_asignacion'], json['con_creacion_fecha']
                 , json['con_motivo_consulta'], json['con_historial_actual'], json['con_evolucion'], json['con_creacion_usuario'])
    ## Consulta - procedimientos
    req_procedimientos = json['lista_procedimientos']
    if len(req_procedimientos)>0:
        for item in req_procedimientos:
            lista_procedimientos.append(ConsultaProcedimientosDto(item['pacasi_codigo_asignacion'], item['con_codigo_establecimiento'], item['con_creacion_fecha'], item['cie_id']))
    consulta.lista_procedimientos = lista_procedimientos
    consdao.updateConsultaProcedimientoDetalle(consulta)
    if consulta.con_codigo_establecimiento:
        return jsonify({'estado':'correcto', 'mensaje':'Se ha realizado la actualizacion en consulta'}), 200
    return jsonify({'estado':'error', 'mensaje':'No se ha realizado'}), 500