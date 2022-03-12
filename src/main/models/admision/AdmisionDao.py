from src.main.db.ConexionDb import ConexionDb
from src.main.models.admision.Pacientedto import Pacientedto

class AdmisionDao:

    def getProfesionales(self):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT p.prof_codigo_medico, e.espec_id, e.espec_descripcion, u.usu_nombres, u.usu_apellidos FROM profesionales p LEFT JOIN usuarios u ON u.usu_codigo_usuario = p.prof_codigo_medico LEFT JOIN especialidades e ON e.espec_id = p.espec_id WHERE p.prof_activo = 't';")
            items = cursor.fetchall()
            lista = []
            for item in items:
                lista.append(dict(codigo_usuario=item[0], especialidad_id=item[1], especialidad_descripcion=item[2], nombre_usuario=item[3], apellido_usuario=item[4]))
            cursor.close()
            conexion.con.close()
            return lista
        except conexion.con.Error as e:
            print(e.pgerror)

    def guardarPaciente(self, pacienteDto):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()##19
            cursor.execute("""INSERT INTO public.pacientes(
            pac_codigo_paciente, pac_tipo_documento, pac_nombres, pac_apellidos, pac_sexo
            , pac_fechanac, pac_lugar_nacimiento, ciu_id, pac_correo_electronico, nac_id
            , pac_telefono, pac_direccion, seg_id, pac_hijos, pac_estado_civil, edu_id
            , sitlab_id, pac_latitud, pac_longitud, pac_creacion_usuario, pac_creacion_fecha, pac_creacion_hora) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_DATE, CURRENT_TIME)""", 
            (pacienteDto.pacCodigoPaciente, pacienteDto.pacTipoDocumento, pacienteDto.pacNombres, pacienteDto.pacApellidos, pacienteDto.pacSexo,
            pacienteDto.pacFechaNac, pacienteDto.pacLugarNacimiento, pacienteDto.ciuId, pacienteDto.pacCorreoElectronico, pacienteDto.nacId,
            pacienteDto.pacTelefono, pacienteDto.pacDireccion, pacienteDto.segId, pacienteDto.pacHijos, pacienteDto.pacEstadoCivil, pacienteDto.eduId,
            pacienteDto.sitlabId, pacienteDto.pacLatitud, pacienteDto.pacLongitud, pacienteDto.pacCreacionUsuario,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            pacienteDto.operacion = "INSERT"
            return pacienteDto
        except conexion.con.Error as e:
            print(e.pgerror)

    def actualizarPacienteFormularioPrincipal(self, pacienteDto):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("""UPDATE public.pacientes SET
            pac_nombres=%s, pac_apellidos=%s, pac_sexo=%s
            , pac_fechanac=%s, pac_lugar_nacimiento=%s, ciu_id=%s, pac_correo_electronico=%s, nac_id=%s
            , pac_telefono=%s, pac_direccion=%s, pac_modificacion_usuario=%s, pac_modificacion_fecha=CURRENT_DATE, pac_modificacion_hora=CURRENT_TIME
            WHERE pac_codigo_paciente=%s""", 
            (pacienteDto.pacNombres, pacienteDto.pacApellidos, pacienteDto.pacSexo,
            pacienteDto.pacFechaNac, pacienteDto.pacLugarNacimiento, pacienteDto.ciuId, pacienteDto.pacCorreoElectronico, pacienteDto.nacId,
            pacienteDto.pacTelefono, pacienteDto.pacDireccion, pacienteDto.pacModificacionUsuario, pacienteDto.pacCodigoPaciente,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            pacienteDto.operacion = "UPDATE-FORMPRINCIPAL"
            return pacienteDto
        except conexion.con.Error as e:
            print(e.pgerror)

    def actualizarPacienteOtrosDatos(self, pacienteDto):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("""UPDATE public.pacientes SET
            seg_id=%s, pac_hijos=%s, pac_estado_civil=%s
            , edu_id=%s, sitlab_id=%s, pac_latitud=%s, pac_longitud=%s, pac_modificacion_usuario=%s, pac_modificacion_fecha=CURRENT_DATE, pac_modificacion_hora=CURRENT_TIME
            WHERE pac_codigo_paciente=%s""", 
            (pacienteDto.segId, pacienteDto.pacHijos, pacienteDto.pacEstadoCivil, pacienteDto.eduId, pacienteDto.sitlabId,
            pacienteDto.pacLatitud, pacienteDto.pacLongitud, pacienteDto.pacModificacionUsuario, pacienteDto.pacCodigoPaciente,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            pacienteDto.operacion = "UPDATE-OTROSDATOS"
            return pacienteDto
        except conexion.con.Error as e:
            print(e.pgerror)

    def getDatosPacienteByCodigoPaciente(self, codigo_paciente):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT pac_codigo_paciente, pac_tipo_documento, pac_nombres, pac_apellidos, pac_sexo, pac_fechanac, pac_lugar_nacimiento, ciu_id, pac_correo_electronico, nac_id, pac_telefono, pac_direccion, seg_id, pac_hijos, pac_estado_civil, edu_id, sitlab_id, pac_latitud, pac_longitud, pac_creacion_usuario, pac_creacion_fecha, pac_creacion_hora, pac_modificacion_usuario, pac_modificacion_fecha, pac_modificacion_hora FROM pacientes WHERE pac_codigo_paciente=%s", (codigo_paciente,))
            item = cursor.fetchone()
            paciente = Pacientedto(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], item[15], item[16], item[17], item[18])
            cursor.close()
            conexion.con.close()
            return paciente
        except conexion.con.Error as e:
            print(e.pgerror)

    def getCantidadPacientes(self):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT COUNT(*) cnt FROM paciente_asignacion")
            item = cursor.fetchone()[0]
            cursor.close()
            conexion.con.close()
            return item
        except conexion.con.Error as e:
            print(e.pgerror)

    def generarPacienteAsignacion(self, prefijo):
        conexion = ConexionDb()
        cuentanro = ""
        cantidadAsignaciones = self.getCantidadPacientes()
        if cantidadAsignaciones==0: return "PA00000001"
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT nextval('asignacionseq')")
            cnt = cursor.fetchone()[0]
            while len(cnt) < 8:
                cnt = "0" + cnt
            cuentanro = prefijo + cnt;
            cursor.close()
            conexion.con.close()
            return cuentanro
        except conexion.con.Error as e:
            print(e.pgerror)

    def insertarPacienteAsignacion(self, pacienteAsignacionDto):
        codigo_asignacion = self.generarPacienteAsignacion("PA")
        try:
            conexion = ConexionDb()
            conexion.con.autocommit = False
            cursor = conexion.con.cursor()
            # grupo de inserciones
            insertPacienteAsignacionSQL = "INSERT INTO public.paciente_asignacion(pacasi_codigo_establecimiento, pacasi_codigo_asignacion, pac_codigo_paciente, med_id, supl_med_id, pacasi_estado, seg_id, pacasi_creacion_usuario, pacasi_creacion_fecha, pacasi_creacion_hora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, CURRENT_DATE, CURRENT_TIME)"
            insertPreconsultaSQL = "INSERT INTO public.preconsulta(precon_codigo_establecimiento, pacasi_codigo_asignacion, precon_creacion_usuario, precon_creacion_fecha, precon_creacion_hora) VALUES(%s, %s, %s, CURRENT_DATE, CURRENT_TIME)"
            insertConsultaSQL = "INSERT INTO public.consulta(con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_usuario, con_creacion_fecha, con_creacion_hora) VALUES(%s, %s, %s, CURRENT_DATE, CURRENT_TIME)"
            cursor.execute(insertPacienteAsignacionSQL, (pacienteAsignacionDto.pacasiCodigoEstablecimiento, codigo_asignacion, pacienteAsignacionDto.pacCodigoPaciente, pacienteAsignacionDto.medId, pacienteAsignacionDto.suplMedId, pacienteAsignacionDto.pacasiEstado, pacienteAsignacionDto.segId, pacienteAsignacionDto.pacasiCreacion_usuario,))
            cursor.execute(insertPreconsultaSQL, (pacienteAsignacionDto.pacasiCodigoEstablecimiento, codigo_asignacion, pacienteAsignacionDto.pacasiCreacion_usuario,))
            cursor.execute(insertConsultaSQL, (pacienteAsignacionDto.pacasiCodigoEstablecimiento, codigo_asignacion, pacienteAsignacionDto.pacasiCreacion_usuario,))
            # confirma todos lo cambios
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            pacienteAsignacionDto.operacion = "ASIGNACION-EXITOSA"
            return pacienteAsignacionDto
        except conexion.con.Error as e:
            # si falla deshace los cambios
            conexion.con.rollback()
            print(e.pgerror)

    def getPacientesAdmitidos(self):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT p.pac_codigo_paciente, p.pac_nombres||' '||p.pac_apellidos paciente , usu.usu_nombres||' '||usu.usu_apellidos medico FROM pacientes p LEFT JOIN paciente_asignacion pa ON pa.pac_codigo_paciente=p.pac_codigo_paciente LEFT JOIN profesionales prof ON prof.prof_codigo_medico=pa.med_id LEFT JOIN usuarios usu ON usu.usu_codigo_usuario=prof_codigo_medico WHERE prof_activo = 't'")
            items = cursor.fetchall()
            lista = []
            for item in items:
                lista.append(dict(pac_codigo_paciente=item[0], paciente=item[1], medico=f'Consultando con el Dr. {item[2]}'))
            cursor.close()
            conexion.con.close()
            return lista
        except conexion.con.Error as e:
            print(e.pgerror)