# Microservicios con Docker Compose

Este repositorio contiene la implementación de tres microservicios utilizando Python y MySQL. Los microservicios son:

1. **Estudiante**: Gestiona los datos principales de un estudiante.
2. **Evaluación**: Gestiona los datos de las evaluaciones de los estudiantes.
3. **Base de Datos (MySQL)**: Almacena la información de los estudiantes y evaluaciones.

## Configuración y Ejecución

### Configurar Visual Studio Code
Abre VSCode y abre la carpeta clonada.
Instala las siguientes extensiones:

Python (publicado por Microsoft)

Docker

### Iniciar los Contenedores con Docker Compose
Ejecuta el siguiente comando en la terminal de VSCode para construir e iniciar los contenedores:

    docker-compose up -d --build

Este comando levantará los tres microservicios y la base de datos MySQL.

## Crear las Tablas en la Base de Datos

Entra al contenedor de MySQL:

    docker exec -it microservicios-python-mysql_db_1 mysql -uroot -p

Introduce la contraseña (password).

Crea las tablas necesarias ejecutando los siguientes comandos SQL:
    
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

Salir del shell de MySQL:

    EXIT;
