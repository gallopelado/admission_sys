from src.main.db.ConexionDb import ConexionDb
from src.main.models.consulta.Consultadto import ConsultaDto
from src.main.models.consulta.ConsultaProcedimientosdto import ConsultaProcedimientosDto
from flask import current_app as app

class ConsultaDao:
    
    def updatePreconsultaData(self, obj)-> ConsultaDto:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('UPDATE public.consulta SET con_motivo_consulta=%s, con_historial_actual=%s, con_evolucion=%s, con_modificacion_usuario=%s, con_modificacion_fecha=%s, con_modificacion_hora=%s WHERE con_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s AND con_creacion_fecha=%s',
                            (obj.con_motivo_consulta, obj.con_historial_actual, obj.con_evolucion, obj.con_modificacion_usuario, obj.con_modificacion_fecha, obj.con_modificacion_hora, obj.con_codigo_establecimiento, obj.pacasi_codigo_asignacion, obj.con_creacion_fecha,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            app.logger.info(f"User: {obj.con_modificacion_usuario} - updated consulta")
            return obj
        except conexion.con.Error as e:
            app.logger.error("consulta: - " + e.pgerror)
            
    def updatePreconsultaProcedimientosData(self, obj)-> ConsultaProcedimientosDto:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('INSERT INTO public.consulta_procedimientos (pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id) VALUES(%s, %s, %s, %s) ON CONFLICT (pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id) DO UPDATE SET con_creacion_fecha = EXCLUDED.con_creacion_fecha, cie_id = EXCLUDED.cie_id',
                            (obj.pacasi_codigo_asignacion, obj.con_codigo_establecimiento, obj.con_creacion_fecha, obj.cie_id,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            app.logger.info(f"updated consulta-procedimientos")
            return obj
        except conexion.con.Error as e:
            app.logger.error("consulta: - " + e.pgerror)
            
    def updateConsultaProcedimientoDetalle(self, consulta):
        conexion = ConexionDb()
        try:
            conexion.con.autocommit = False
            cursor = conexion.con.cursor()
            
            # Update consulta
            cursor.execute('UPDATE public.consulta SET con_motivo_consulta=%s, con_historial_actual=%s, con_evolucion=%s, con_modificacion_usuario=%s, con_modificacion_fecha=%s, con_modificacion_hora=%s WHERE con_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s AND con_creacion_fecha=%s',
                            (consulta.con_motivo_consulta, consulta.con_historial_actual, consulta.con_evolucion, consulta.con_modificacion_usuario, consulta.con_modificacion_fecha, consulta.con_modificacion_hora, consulta.con_codigo_establecimiento, consulta.pacasi_codigo_asignacion, consulta.con_creacion_fecha,))
            
            # Update or Insert procedimiento
            if len(consulta.lista_procedimientos)>0:
                for obj in consulta.lista_procedimientos:
                    cursor.execute('INSERT INTO public.consulta_procedimientos (pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id) VALUES(%s, %s, %s, %s) ON CONFLICT (pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id) DO UPDATE SET con_creacion_fecha = EXCLUDED.con_creacion_fecha, cie_id = EXCLUDED.cie_id',
                                    (obj.pacasi_codigo_asignacion, obj.con_codigo_establecimiento, obj.con_creacion_fecha, obj.cie_id,))
            
            conexion.con.commit()
            conexion.con.autocommit = True
            cursor.close()
            conexion.con.close()
            app.logger.info(f"updated consulta-procedimientos-transactional")
            return consulta
        except conexion.con.Error as e:
            conexion.con.rollback()
            app.logger.error("consulta: - " + e.pgerror)
            
    def getConsultaData(self, codigo_establecimiento, codigo_asignacion, creacion_fecha)-> dict:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('SELECT con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha, con_motivo_consulta, con_historial_actual, con_evolucion FROM public.consulta WHERE con_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s AND con_creacion_fecha=%s', (codigo_establecimiento, codigo_asignacion, creacion_fecha))
            item = cursor.fetchone()
            cursor.close()
            conexion.con.close()
            app.logger.info("get consulta")
            return {
                'con_codigo_establecimiento': item[0]
                , 'pacasi_codigo_asignacion': item[1]
                , 'con_creacion_fecha': item[2]
                , 'con_motivo_consulta': item[3]
                , 'con_historial_actual': item[4]
                , 'con_evolucion': item[5]
            }
        except conexion.con.Error as e:
            app.logger.error("consulta: - " + e.pgerror)
            
    def getConsultaProcedimientosData(self, codigo_establecimiento, codigo_asignacion, creacion_fecha)-> dict:
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute('SELECT con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha, cie_id FROM public.consulta_procedimientos WHERE con_codigo_establecimiento=%s AND pacasi_codigo_asignacion=%s AND con_creacion_fecha=%s', (codigo_establecimiento, codigo_asignacion, creacion_fecha))
            items = cursor.fetchall()
            cursor.close()
            conexion.con.close()
            app.logger.info("preconsulta-procedimientos")
            # return {
            #     'con_codigo_establecimiento': item[0]
            #     , 'pacasi_codigo_asignacion': item[1]
            #     , 'con_creacion_fecha': item[4]
            #     , 'cie_id':item[3]
            # }
            # { i: results.count(i) for i in range(2, max_result+1) }
            return [{'con_codigo_establecimiento': item[0], 'pacasi_codigo_asignacion': item[1], 'con_creacion_fecha': item[2], 'cie_id':item[3]} for item in items]
        except conexion.con.Error as e:
            app.logger.error("preconsulta-procedimientos: - " + e.pgerror)