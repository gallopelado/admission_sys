from crypt import methods
from flask import Blueprint, jsonify, request
from src.main.models.admision.AdmisionDao import AdmisionDao
from src.main.models.admision.Pacientedto import Pacientedto
from src.main.models.admision.PacienteAsignacionDto import PacienteAsignacionDto
from src.main.models.admision.Paciente_schema import Paciente_Schema

# Modularizar
admisionMod = Blueprint("admisionMod", __name__)
admidao = AdmisionDao()

@admisionMod.route("/get_profesionales")
def getProfesionales():
    items = admidao.getProfesionales()
    return jsonify(items), 200

@admisionMod.route("/guardar_paciente", methods=["POST"])
def guardarPaciente():
    json = request.get_json()
    pacienteDto = Pacientedto()
    pacienteDto.pacCodigoPaciente = json['codigo_paciente']
    pacienteDto.pacTipoDocumento = json['tipo_documento']
    pacienteDto.pacNombres = json['nombres']
    pacienteDto.pacApellidos = json['apellidos']
    pacienteDto.pacSexo = json['sexo']
    pacienteDto.pacFechaNac = json['fecha_nac']
    pacienteDto.pacLugarNacimiento = json['lugar_nac']
    pacienteDto.ciuId = json['ciu_id']
    pacienteDto.pacCorreoElectronico = json['correo_electronico']
    pacienteDto.nacId = json['nac_id']
    pacienteDto.pacTelefono = json['telefono']
    pacienteDto.pacDireccion = json['direccion']
    pacienteDto.segId = json['seg_id']
    pacienteDto.pacHijos = json['hijos']
    pacienteDto.pacEstadoCivil = json['estado_civil']
    pacienteDto.eduId = json['edu_id']
    pacienteDto.sitlabId = json['sitlab_id']
    pacienteDto.pacLatitud = json['latitud']
    pacienteDto.pacLongitud = json['longitud']
    pacienteDto.pacCreacionUsuario = json['creacion_usuario']
    resp = admidao.guardarPaciente(pacienteDto)
    if resp and resp.operacion=="INSERT":
        return jsonify("{'estado': 'correcto', mensaje:'inserción correcta'}"), 201
    return jsonify("{'estado': 'error', mensaje:'problemas en la inserción'}"), 500

@admisionMod.route("/actualizar_paciente_formulario_principal", methods=["PUT"])
def actualizarPacienteFormularioPrincipal():
    json = request.get_json()
    pacienteDto = Pacientedto()
    pacienteDto.pacCodigoPaciente = json['codigo_paciente']
    pacienteDto.pacNombres = json['nombres']
    pacienteDto.pacApellidos = json['apellidos']
    pacienteDto.pacSexo = json['sexo']
    pacienteDto.pacFechaNac = json['fecha_nac']
    pacienteDto.pacLugarNacimiento = json['lugar_nac']
    pacienteDto.ciuId = json['ciu_id']
    pacienteDto.pacCorreoElectronico = json['correo_electronico']
    pacienteDto.nacId = json['nac_id']
    pacienteDto.pacTelefono = json['telefono']
    pacienteDto.pacDireccion = json['direccion']
    pacienteDto.pacModificacionUsuario = json['modificacion_usuario']
    resp = admidao.actualizarPacienteFormularioPrincipal(pacienteDto)
    if resp and resp.operacion=="UPDATE-FORMPRINCIPAL":
        return jsonify("{'estado': 'correcto', mensaje:'operacion correcta'}"), 200
    return jsonify("{'estado': 'error', mensaje:'problemas en la operacion'}"), 500

@admisionMod.route("/actualizar_paciente_otros_datos", methods=["PUT"])
def actualizarPacienteOtrosDatos():
    json = request.get_json()
    pacienteDto = Pacientedto()
    pacienteDto.pacCodigoPaciente = json['codigo_paciente']
    pacienteDto.segId = json['seg_id']
    pacienteDto.pacHijos = json['hijos']
    pacienteDto.pacEstadoCivil = json['estado_civil']
    pacienteDto.eduId = json['edu_id']
    pacienteDto.sitlabId = json['sitlab_id']
    pacienteDto.pacLatitud = json['latitud']
    pacienteDto.pacLongitud = json['longitud']
    pacienteDto.pacModificacionUsuario = json['modificacion_usuario']
    resp = admidao.actualizarPacienteOtrosDatos(pacienteDto)
    if resp and resp.operacion=="UPDATE-OTROSDATOS":
        return jsonify("{'estado': 'correcto', mensaje:'operacion correcta'}"), 200
    return jsonify("{'estado': 'error', mensaje:'problemas en la operacion'}"), 500

@admisionMod.route('/get_datos_paciente_by_codigo_paciente/<string:codigo_paciente>')
def getDatosPacienteByCodigoPaciente(codigo_paciente):
    paciente = admidao.getDatosPacienteByCodigoPaciente(codigo_paciente)
    schema = Paciente_Schema()
    if paciente is not None:
        return jsonify(schema.dump(paciente)), 200
    else:
        return jsonify("{'estado':'correcto', 'mensaje':'No existe paciente'}"), 200

@admisionMod.route("/insertar_paciente_asignacion", methods=["POST"])
def insertarPacienteAsignacion():
    json = request.get_json()
    pacienteAsigDto = PacienteAsignacionDto()
    pacienteAsigDto.pacasiCodigoEstablecimiento = json['codigo_establecimiento']
    pacienteAsigDto.pacCodigoPaciente = json['codigo_paciente']
    pacienteAsigDto.medId = json['med_id']
    pacienteAsigDto.segId = json['seg_id']
    pacienteAsigDto.pacasiEstado = 'A'
    pacienteAsigDto.pacasiCreacion_usuario = json['creacion_usuario']
    resp = admidao.insertarPacienteAsignacion(pacienteAsigDto)
    if resp and resp.operacion=="ASIGNACION-EXITOSA":
        return jsonify("{'estado': 'correcto', mensaje:'asignación de paciente correcta'}"), 201
    return jsonify("{'estado': 'error', mensaje:'problemas en la asignación de paciente'}"), 500

@admisionMod.route('/get_pacientes_admitidos')
def getPacientesAdmitidos():
    pacientes = admidao.getPacientesAdmitidos()
    if pacientes is not None and len(pacientes):
        return jsonify(pacientes), 200
    else:
        return jsonify("{'estado':'error', 'mensaje':'problemas al obtener pacientes'}"), 200