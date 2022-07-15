class PacienteAsignacionDto:
    def __init__(self, pacasiCodigoEstablecimiento=None, pacasiCodigoAsignacion=None, pacCodigoPaciente=None, pacConsultaFecha=None, medId=None, 
    suplMedId=None, pacasiCodigoConsultorio=None, pacasiHoraConsulta=None, pacasiNumeroOrdenEspera=None, pacasiEstado=None, segId=None,
    pacasiCreacion_usuario=None, pacasiCreacion_fecha=None, pacasiCreacion_hora=None, 
    pacasiModificacionUsuario=None, pacasiModificacionFecha=None, pacasiModificacionHora=None, operacion=None):
        self.pacasiCodigoEstablecimiento = pacasiCodigoEstablecimiento
        self.pacasiCodigoAsignacion = pacasiCodigoAsignacion
        self.pacCodigoPaciente = pacCodigoPaciente
        self.pacConsultaFecha = pacConsultaFecha
        self.medId = medId
        self.suplMedId = suplMedId
        self.pacasiCodigoConsultorio = pacasiCodigoConsultorio
        self.pacasiHoraConsulta = pacasiHoraConsulta
        self.pacasiNumeroOrdenEspera = pacasiNumeroOrdenEspera
        self.pacasiEstado = pacasiEstado
        self.segId = segId
        self.pacasiCreacion_usuario = pacasiCreacion_usuario
        self.pacasiCreacion_fecha = pacasiCreacion_fecha
        self.pacasiCreacion_hora = pacasiCreacion_hora
        self.pacasiModificacionUsuario = pacasiModificacionUsuario
        self.pacasiModificacionFecha = pacasiModificacionFecha
        self.pacasiModificacionHora = pacasiModificacionHora
        self.operacion = operacion