from src.main.db.ConexionDb import ConexionDb
from src.main.models.preconsulta import Preconsultadto
from flask import current_app as app

class PreconsultaDao:
    
    def updatePreconsultaData(self, obj)-> Preconsultadto:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('UPDATE public.preconsulta SET precon_temperatura_corporal=%s, precon_presion_arterial=%s, precon_frecuencia_respiratoria=%s, precon_pulso=%s, precon_peso=%s, precon_talla=%s, precon_imc=%s, precon_saturacion=%s, precon_circunferencia_abdominal=%s, precon_motivo_consulta=%s, precon_modificacion_usuario=%s, precon_modificacion_fecha=CURRENT_DATE, precon_modificacion_hora=CURRENT_TIME WHERE precon_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s',
                            (obj.precon_temperatura_corporal, obj.precon_presion_arterial, obj.precon_frecuencia_respiratoria, obj.precon_pulso, obj.precon_peso, obj.precon_talla, obj.precon_imc, obj.precon_saturacion, obj.precon_circunferencia_abdominal, obj.precon_motivo_consulta, obj.precon_creacion_usuario, obj.precon_codigo_establecimiento, obj.pacasi_codigo_asignacion,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            app.logger.info(f"User: {obj.precon_creacion_usuario} - updated preconsulta")
            return obj
        except conexion.con.Error as e:
            app.logger.error("preconsulta: - " + e.pgerror)
            
    def getPreconsultaData(self, codigo_establecimiento, codigo_asignacion)-> dict:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('SELECT precon_codigo_establecimiento, pacasi_codigo_asignacion, precon_creacion_fecha, precon_temperatura_corporal, precon_presion_arterial, precon_frecuencia_respiratoria, precon_pulso, precon_peso, precon_talla, precon_imc, precon_saturacion, precon_circunferencia_abdominal, precon_motivo_consulta, precon_creacion_usuario, precon_creacion_hora, precon_modificacion_usuario, precon_modificacion_fecha, precon_modificacion_hora FROM public.preconsulta WHERE precon_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s', (codigo_establecimiento, codigo_asignacion,))
            item = cursor.fetchone()
            cursor.close()
            conexion.con.close()
            app.logger.info("get preconsulta")
            return {
                'precon_codigo_establecimiento': item[0]
                , 'pacasi_codigo_asignacion': item[1]
                , 'precon_creacion_fecha': item[2]
                , 'precon_temperatura_corporal': item[3]
                , 'precon_presion_arterial': item[4]
                , 'precon_frecuencia_respiratoria': item[5]
                , 'precon_pulso': item[6]
                , 'precon_peso': item[7]
                , 'precon_talla': item[8]
                , 'precon_imc': item[9]
                , 'precon_saturacion': item[10]
                , 'precon_circunferencia_abdominal': item[11]
                , 'precon_motivo_consulta': item[12]
            }
        except conexion.con.Error as e:
            app.logger.error("preconsulta: - " + e.pgerror)