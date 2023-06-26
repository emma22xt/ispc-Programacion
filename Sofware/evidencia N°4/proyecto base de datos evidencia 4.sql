CREATE TABLE if not exists Dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    numero_serie VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL
);

CREATE TABLE if not exists Instalaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    direccion_instalacion VARCHAR(100) NOT NULL,
    fecha_instalacion DATE NOT NULL,
    coordenadas VARCHAR(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES Dispositivos(id)