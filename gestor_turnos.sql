CREATE DATABASE gestor_turnos; 
USE gestor_turnos;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    ocupacion VARCHAR(50) NOT NULL  -- Nueva columna para la ocupación
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE turnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    empleado_id INT,  -- Nueva columna para la relación con empleado
    fecha DATE,
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)  -- Relación con la tabla empleados
);



SHOW TABLES;

DROP TABLE usuarios;

