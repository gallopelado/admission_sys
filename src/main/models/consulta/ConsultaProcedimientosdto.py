class ConsultaProcedimientosDto:
    def __init__(self, pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id):
        self.pacasi_codigo_asignacion = pacasi_codigo_asignacion
        self.con_codigo_establecimiento = con_codigo_establecimiento
        self.con_creacion_fecha = con_creacion_fecha
        self.cie_id = cie_id