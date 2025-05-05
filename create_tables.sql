USE microservicios;

CREATE TABLE estudiantes (
    rut VARCHAR(12) PRIMARY KEY,
    nombre_completo VARCHAR(255),
    edad INT,
    curso VARCHAR(10)
);

CREATE TABLE evaluaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut_estudiante VARCHAR(12),
    semestre INT,
    asignatura VARCHAR(100),
    evaluacion DECIMAL(3, 1),
    FOREIGN KEY (rut_estudiante) REFERENCES estudiantes(rut)
);
