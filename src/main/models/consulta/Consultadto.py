class ConsultaDto:
    
    def __init__(self, con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha=None
                 , con_motivo_consulta=None, con_historial_actual=None, con_evolucion=None
                 , con_creacion_usuario=None, con_creacion_hora=None
                 , con_modificacion_usuario=None, con_modificacion_fecha=None, con_modificacion_hora=None):
        self.con_codigo_establecimiento = con_codigo_establecimiento
        self.pacasi_codigo_asignacion = pacasi_codigo_asignacion
        self.con_creacion_fecha = con_creacion_fecha
        self.con_motivo_consulta = con_motivo_consulta
        self.con_historial_actual = con_historial_actual
        self.con_evolucion = con_evolucion
        self.con_creacion_usuario = con_creacion_usuario
        self.con_creacion_hora = con_creacion_hora
        self.con_modificacion_usuario = con_modificacion_usuario
        self.con_modificacion_fecha = con_modificacion_fecha
        self.con_modificacion_hora = con_modificacion_hora
    