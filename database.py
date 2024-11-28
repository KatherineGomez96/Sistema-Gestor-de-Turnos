import mysql.connector
from mysql.connector import Error

def crear_db_y_tablas():
    try:
        # Conectar a MySQL
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="mibase1234"
        )
        if conn.is_connected():
            cursor = conn.cursor()
            
            # Crear la base de datos
            cursor.execute("CREATE DATABASE IF NOT EXISTS gestor_turnos")
            print("Base de datos 'gestor_turnos' creada o ya existe.")
            
            # Seleccionar la base de datos
            cursor.execute("USE gestor_turnos")
            
            # Crear la tabla de usuarios
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL
            )''')
            print("Tabla 'usuarios' creada o ya existe.")
            
            # Crear la tabla de turnos
            cursor.execute('''CREATE TABLE IF NOT EXISTS turnos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT,
                fecha DATE,
                hora_inicio TIME,
                hora_fin TIME,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
            )''')
            print("Tabla 'turnos' creada o ya existe.")
            
            # Confirmar cambios
            conn.commit()
            return "Base de datos y tablas creadas exitosamente."
        else:
            return "No se pudo conectar a la base de datos."
    
    except Error as e:
        return f"Error al conectar a MySQL: {e}"
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión a MySQL cerrada.")

# Llama a la función para crear la base de datos y tablas al ejecutar este archivo
if __name__ == "__main__":
    mensaje = crear_db_y_tablas()
    print(mensaje)

