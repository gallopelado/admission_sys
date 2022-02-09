-- ciudades
CREATE TABLE IF NOT EXISTS public.ciudades(
    ciu_id SERIAL PRIMARY KEY, ciu_descripcion TEXT UNIQUE
);

-- nacionalidades
CREATE TABLE IF NOT EXISTS public.nacionalidades(
    nac_id SERIAL PRIMARY KEY, nac_descripcion TEXT UNIQUE
);

-- nivel educativo
CREATE TABLE IF NOT EXISTS public.nivel_educativo(
    edu_id SERIAL PRIMARY KEY, edu_descripcion TEXT UNIQUE
);

-- seguro medico
CREATE TABLE IF NOT EXISTS public.seguro_medico(
    seg_id SERIAL PRIMARY KEY, seg_descripcion TEXT UNIQUE
);

-- situacion laboral
CREATE TABLE IF NOT EXISTS public.situacion_laboral(
    sitlab_id SERIAL PRIMARY KEY, sitlab_descripcion TEXT UNIQUE
);

-- pacientes
CREATE TABLE IF NOT EXISTS public.pacientes(
    pac_codigo_paciente VARCHAR PRIMARY KEY,
    pac_tipo_documento VARCHAR NOT NULL,
    pac_nombres VARCHAR NOT NULL,
    pac_apellidos VARCHAR NOT NULL,
    pac_sexo VARCHAR(1) NOT NULL,
    pac_fechanac DATE NOT NULL,
    pac_lugar_nacimiento TEXT,
    pac_correo_electronico TEXT,
    pac_telefono VARCHAR,
    pac_direccion TEXT,
    pac_hijos INTEGER,
    pac_estado_civil VARCHAR,
    pac_latitud DOUBLE PRECISION,
    pac_longitud DOUBLE PRECISION,
    ciu_id INTEGER NOT NULL,
    nac_id INTEGER NOT NULL,
    seg_id INTEGER,
    edu_id INTEGER,
    sitlab_id INTEGER,
    pac_creacion_usuario VARCHAR(10) NOT NULL,
    pac_creacion_fecha DATE NOT NULL,
    pac_creacion_hora TIME NOT NULL,
    pac_modificacion_usuario VARCHAR(10),
    pac_modificacion_fecha DATE,
    pac_modificacion_hora TIME,
    FOREIGN KEY(ciu_id) REFERENCES public.ciudades(ciu_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(nac_id) REFERENCES public.nacionalidades(nac_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(seg_id) REFERENCES public.seguro_medico(seg_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(edu_id) REFERENCES public.nivel_educativo(edu_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(sitlab_id) REFERENCES public.situacion_laboral(sitlab_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- especialidades
CREATE TABLE IF NOT EXISTS public.especialidades(
    espec_id SERIAL PRIMARY KEY, espec_descripcion TEXT UNIQUE
);

-- usuarios
CREATE TABLE IF NOT EXISTS public.usuarios(
    usu_codigo_usuario VARCHAR(10) PRIMARY KEY,
    usu_password VARCHAR(64) NOT NULL,
    usu_nombres VARCHAR(30) NOT NULL,
    usu_apellidos VARCHAR(30) NOT NULL,
    usu_descripcion TEXT NOT NULL,
    usu_rol VARCHAR,
    usu_estado VARCHAR(1) NOT NULL,
    usu_creacion_usuario VARCHAR(10) NOT NULL,
    usu_creacion_fecha DATE NOT NULL,
    usu_creacion_hora TIME NOT NULL,
    usu_modificacion_usuario VARCHAR(10),
    usu_modificacion_fecha DATE,
    usu_modificacion_hora TIME
);

-- profesionales
CREATE TABLE IF NOT EXISTS public.profesionales(
    prof_codigo_medico VARCHAR(10) PRIMARY KEY,
    prof_numero_registro VARCHAR(10) NOT NULL,
    prof_activo VARCHAR(1),
    espec_id INTEGER NOT NULL,
    prof_creacion_usuario VARCHAR(10) NOT NULL,
    prof_creacion_fecha DATE NOT NULL,
    prof_creacion_hora TIME NOT NULL,
    prof_modificacion_usuario VARCHAR(10),
    prof_modificacion_fecha DATE,
    prof_modificacion_hora TIME,
    FOREIGN KEY(espec_id) REFERENCES especialidades(espec_id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(prof_codigo_medico) REFERENCES usuarios(usu_codigo_usuario) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- paciente asignacion
CREATE TABLE IF NOT EXISTS public.paciente_asignacion(
    pacasi_codigo_establecimiento VARCHAR(16),
    pacasi_codigo_asignacion VARCHAR(10),
    pac_codigo_paciente VARCHAR NOT NULL,
    pac_consulta_fecha DATE,
    pacasi_codigo_consultorio INTEGER,
    pacasi_hora_consulta TIME,
    pacasi_numero_orden_espera INTEGER,
    pacasi_estado VARCHAR(1),
    med_id VARCHAR(10) NOT NULL,
    supl_med_id VARCHAR(10),
    seg_id INTEGER,
    pacasi_creacion_usuario VARCHAR(10) NOT NULL,
    pacasi_creacion_fecha DATE NOT NULL,
    pacasi_creacion_hora TIME NOT NULL,
    pacasi_modificacion_usuario VARCHAR(10),
    pacasi_modificacion_fecha DATE,
    pacasi_modificacion_hora TIME,
    PRIMARY KEY(pacasi_codigo_establecimiento, pacasi_codigo_asignacion),
    FOREIGN KEY(med_id) REFERENCES public.profesionales(prof_codigo_medico) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(supl_med_id) REFERENCES public.profesionales(prof_codigo_medico) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(seg_id) REFERENCES public.seguro_medico(seg_id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- preconsulta
CREATE TABLE IF NOT EXISTS public.preconsulta(
    precon_codigo_establecimiento VARCHAR(16) NOT NULL,
    pacasi_codigo_asignacion VARCHAR(10) NOT NULL,
    precon_creacion_fecha DATE,
    precon_temperatura_corporal DOUBLE PRECISION,
    precon_presion_arterial DOUBLE PRECISION,
    precon_frecuencia_respiratoria DOUBLE PRECISION,
    precon_pulso DOUBLE PRECISION,
    precon_peso DOUBLE PRECISION,
    precon_talla DOUBLE PRECISION,
    precon_imc DOUBLE PRECISION,
    precon_saturacion DOUBLE PRECISION,
    precon_circunferencia_abdominal DOUBLE PRECISION,
    precon_motivo_consulta TEXT,
    precon_creacion_usuario VARCHAR(10),
    precon_creacion_hora TIME,
    precon_modificacion_usuario VARCHAR(10),
    precon_modificacion_fecha DATE,
    precon_modificacion_hora TIME,
    PRIMARY KEY(precon_codigo_establecimiento, pacasi_codigo_asignacion),
    FOREIGN KEY(precon_codigo_establecimiento, pacasi_codigo_asignacion) REFERENCES public.paciente_asignacion(pacasi_codigo_establecimiento, pacasi_codigo_asignacion) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- cie
CREATE TABLE IF NOT EXISTS public.cie(
    cie_id SERIAL PRIMARY KEY,
    cie_codigo VARCHAR UNIQUE,
    cie_descripcion VARCHAR,
    cie_tipo VARCHAR
);

-- consulta
CREATE TABLE IF NOT EXISTS public.consulta(
    con_codigo_establecimiento VARCHAR(16) NOT NULL,
    pacasi_codigo_asignacion VARCHAR(10) NOT NULL,
    con_creacion_fecha DATE NOT NULL,
    con_motivo_consulta TEXT,
    con_historial_actual TEXT,
    con_evolucion TEXT,
    con_creacion_usuario VARCHAR(10),
    con_creacion_hora TIME,
    con_modificacion_usuario VARCHAR(10),
    con_modificacion_fecha DATE,
    con_modificacion_hora TIME,
    PRIMARY KEY(con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha),
    FOREIGN KEY(pacasi_codigo_asignacion, con_codigo_establecimiento) REFERENCES preconsulta(pacasi_codigo_asignacion, precon_codigo_establecimiento) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- consulta_procedimientos
CREATE TABLE IF NOT EXISTS public.consulta_procedimientos(
    pacasi_codigo_asignacion VARCHAR(10) NOT NULL,
    con_codigo_establecimiento VARCHAR(16) NOT NULL,
    con_creacion_fecha DATE NOT NULL,
    cie_id INTEGER NOT NULL,
    PRIMARY KEY(pacasi_codigo_asignacion, con_codigo_establecimiento, con_creacion_fecha, cie_id),
    FOREIGN KEY(con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha) 
    REFERENCES consulta(con_codigo_establecimiento, pacasi_codigo_asignacion, con_creacion_fecha) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(cie_id) REFERENCES cie(cie_id) ON DELETE RESTRICT ON UPDATE CASCADE
);