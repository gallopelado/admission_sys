class PreconsultaDto:
    
    def __init__(self, precon_codigo_establecimiento, pacasi_codigo_asignacion, precon_creacion_fecha=None
                 , precon_temperatura_corporal=None, precon_presion_arterial=None, precon_frecuencia_respiratoria=None
                 , precon_pulso=None, precon_peso=None, precon_talla=None, precon_imc=None, precon_saturacion=None
                 , precon_circunferencia_abdominal=None, precon_motivo_consulta=None, precon_creacion_usuario=None
                 , precon_creacion_hora=None, precon_modificacion_usuario=None, precon_modificacion_fecha=None, precon_modificacion_hora=None):
        self.precon_codigo_establecimiento = precon_codigo_establecimiento
        self.pacasi_codigo_asignacion = pacasi_codigo_asignacion
        self.precon_creacion_fecha = precon_creacion_fecha
        self.precon_temperatura_corporal = precon_temperatura_corporal
        self.precon_presion_arterial = precon_presion_arterial
        self.precon_frecuencia_respiratoria = precon_frecuencia_respiratoria
        self.precon_pulso = precon_pulso
        self.precon_peso = precon_peso
        self.precon_talla = precon_talla
        self.precon_imc = precon_imc
        self.precon_saturacion = precon_saturacion
        self.precon_circunferencia_abdominal = precon_circunferencia_abdominal
        self.precon_motivo_consulta = precon_motivo_consulta
        self.precon_creacion_usuario = precon_creacion_usuario
        self.precon_creacion_hora = precon_creacion_hora
        self.precon_modificacion_usuario = precon_modificacion_usuario
        self.precon_modificacion_fecha = precon_modificacion_fecha
        self.precon_modificacion_hora = precon_modificacion_hora
    