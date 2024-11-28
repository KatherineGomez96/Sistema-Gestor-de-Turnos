import mysql.connector
from mysql.connector import Error

def agregar_usuario(nombre):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="mibase1234", 
            database="gestor_turnos"
        )
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (nombre) VALUES (%s)"
        cursor.execute(query, (nombre,))
        conn.commit()
        return f"Usuario {nombre} agregado."
    except Error as err:
        return f"Error al agregar usuario: {err}"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def agregar_empleado(dni, nombre, apellido, telefono, ocupacion):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="mibase1234", 
            database="gestor_turnos"
        )
        cursor = conn.cursor()
        query = "INSERT INTO empleados (dni, nombre, apellido, telefono, ocupacion) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (dni, nombre, apellido, telefono, ocupacion))
        conn.commit()
        print(f"Empleado {nombre} {apellido} agregado.")
    except Error as err:
        print(f"Error al agregar empleado: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# Prueba de la función agregar_usuario (opcional)
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del usuario a agregar: ")
    mensaje = agregar_usuario(nombre)
    print(mensaje)
