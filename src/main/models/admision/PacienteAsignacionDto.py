class PacienteAsignacionDto:
    def __init__(self, pacasiCodigoEstablecimiento, pacasiCodigoAsignacion, pacCodigoPaciente, pacConsultaFecha, medId, 
    suplMedId, pacasiCodigoConsultorio, pacasiHoraConsulta, pacasiNumeroOrdenEspera, pacasiEstado, segId,
    pacasiCreacion_usuario, pacasiCreacion_fecha, pacasiCreacion_hora, 
    pacasiModificacionUsuario, pacasiModificacionFecha, pacasiModificacionHora, operacion):
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