import mysql.connector
from mysql.connector import Error

def agregar_turno(usuario_id, empleado_id, fecha, hora_inicio, hora_fin):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="mibase1234", 
            database="gestor_turnos"
        )
        cursor = conn.cursor()
        query = '''INSERT INTO turnos (usuario_id, empleado_id, fecha, hora_inicio, hora_fin) 
                   VALUES (%s, %s, %s, %s, %s)'''
        cursor.execute(query, (usuario_id, empleado_id, fecha, hora_inicio, hora_fin))
        conn.commit()
        print(f"Turno agregado para el usuario ID {usuario_id} en {fecha}.")
    except Error as err:
        print(f"Error al agregar turno: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def ver_turnos():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mibase1234",
            database="gestor_turnos"
        )
        cursor = conn.cursor()

        cursor.execute('''SELECT t.id, u.nombre, t.fecha, t.hora_inicio, t.hora_fin 
                          FROM turnos t JOIN usuarios u ON t.usuario_id = u.id''')
        
        turnos = cursor.fetchall()

        for turno in turnos:
            print(f"ID: {turno[0]}, Usuario: {turno[1]}, Fecha: {turno[2]}, Hora Inicio: {turno[3]}, Hora Fin: {turno[4]}")
    
    except Error as err:
        print(f"Error al cargar turnos: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def eliminar_turno(turno_id):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="mibase1234", 
            database="gestor_turnos"
        )
        cursor = conn.cursor()
        query = "DELETE FROM turnos WHERE id = %s"
        cursor.execute(query, (turno_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            return f"No se encontró un turno con ID {turno_id}."
        return f"Turno con ID {turno_id} eliminado."
    except Error as err:
        return f"Error al eliminar turno: {err}"
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Prueba de la función ver_turnos (opcional)
if __name__ == "__main__":
    ver_turnos()
