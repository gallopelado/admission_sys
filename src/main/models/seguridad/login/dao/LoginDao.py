from src.main.db.ConexionDb import ConexionDb
from src.main.models.seguridad.login.entidades.Logindto import Logindto
class LoginDao:
    
    def listarTodos(self):
        conexion = ConexionDb()
        usuarios = []
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT usu_codigo_usuario, usu_password, usu_nombres, usu_apellidos, usu_descripcion, usu_estado, usu_rol, usu_creacion_usuario, usu_creacion_fecha, usu_creacion_hora FROM public.usuarios")
            items = cursor.fetchall()
            if items:
                for item in items:
                    usuario = Logindto(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
                    usuarios.append(usuario)
            cursor.close()
            conexion.con.close()
        except conexion.con.Error as e:
            print(e.pgerror)
        return usuarios
    
    def getUsuarioByCodigoUsuario(self, codigo_usuario):
        conexion = ConexionDb()
        usuario = {}
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT usu_codigo_usuario, usu_password, usu_nombres, usu_apellidos, usu_descripcion, usu_estado, usu_rol, usu_creacion_usuario, usu_creacion_fecha, usu_creacion_hora FROM public.usuarios WHERE usu_codigo_usuario=%s", (codigo_usuario,))
            item = cursor.fetchone()
            if item:
                usuario = Logindto(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9])
            cursor.close()
            conexion.con.close()
        except conexion.con.Error as e:
            print(e.pgerror)
        return usuario

    def agregarUsuario(self, usuario):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("INSERT INTO public.usuarios (usu_codigo_usuario, usu_password, usu_nombres, usu_apellidos, usu_descripcion, usu_rol, usu_estado, usu_creacion_usuario, usu_creacion_fecha, usu_creacion_hora) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (usuario.usuCodigoUsuario, usuario.usuPassword, usuario.usuNombres, usuario.usuApellidos, usuario.usuDescripcion, usuario.usuRol, usuario.usuEstado, usuario.usuCreacion_usuario, usuario.usuCreacion_fecha, usuario.usuCreacion_hora,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            usuario.operacion = "INSERTADO"
            return True
        except conexion.con.Error as e:
            print(e.pgerror)

    def modificarUsuario(self, usuario):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("UPDATE public.usuarios SET usu_password=%s, usu_nombres=%s, usu_apellidos=%s, usu_descripcion=%s, usu_rol=%s, usu_estado=%s, usu_modificacion_usuario=%s, usu_modificacion_fecha=%s, usu_modificacion_hora=%s WHERE usu_codigo_usuario = %s", 
            (usuario.usuPassword, usuario.usuNombres, usuario.usuApellidos, usuario.usuDescripcion, usuario.usuRol, usuario.usuEstado, usuario.usuModificacion_usuario, usuario.usuModificacion_fecha, usuario.usuModificacion_hora, usuario.usuCodigoUsuario,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            usuario.operacion = "ACTUALIZADO"
            return True
        except conexion.con.Error as e:
            return e.pgerror

    def eliminar(self, codigo_usuario):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("DELETE FROM public.usuarios WHERE usu_codigo_usuario = %s", (codigo_usuario,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            usuario.operacion = "ELIMINADO"
            return True
        except conexion.con.Error as e:
            return e.pgerror

    def getUserAndPassword(self, user, password):
        conexion = ConexionDb()
        usuario = {}
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT usu_codigo_usuario, usu_password, usu_nombres, usu_apellidos, usu_descripcion, usu_estado, usu_rol FROM usuarios WHERE usu_estado='t' AND usu_codigo_usuario=%s AND usu_password=%s", (user, password,))
            item = cursor.fetchone()
            if item:
                usuario = Logindto(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            cursor.close()
            conexion.con.close()
        except conexion.con.Error as e:
            print(e.pgerror)
        return usuario

    def modificarPassword(self, usuario):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("UPDATE public.usuarios SET usu_password=%s, usu_modificacion_usuario=%s, usu_modificacion_fecha=%s, usu_modificacion_hora=%s WHERE usu_codigo_usuario = %s", 
            (usuario.usuPassword, usuario.usuModificacion_usuario, usuario.usuModificacion_fecha, usuario.usuModificacion_hora, usuario.usuCodigoUsuario,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            usuario.operacion = "CLAVE ACTUALIZADA"
            return True
        except conexion.con.Error as e:
            return e.pgerror