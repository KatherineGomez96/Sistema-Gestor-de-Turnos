from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta


app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

def conectar_db():
    """Función para conectar a la base de datos y manejar errores."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="mibase1234",
            database="gestor_turnos"
        )
    except Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

# Rutas de renderizado de plantillas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuario.html')

@app.route('/empleados')
def empleados():
    return render_template('empleado.html')

# Ruta para agregar usuario
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    dni = data.get('dni')
    telefono = data.get('telefono')

    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "INSERT INTO usuarios (dni, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (dni, nombre, apellido, telefono))
        conn.commit()
        return jsonify({'message': f'Usuario {nombre} {apellido} agregado exitosamente.'}), 201
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Ruta para obtener usuarios
@app.route('/ver_usuarios', methods=['GET'])
def ver_usuarios():
    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, dni, nombre, apellido, telefono FROM usuarios")
        usuarios = cursor.fetchall()
        return jsonify(usuarios), 200
    except Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Ruta para agregar empleado
@app.route('/agregar_empleado', methods=['POST'])
def agregar_empleado():
    data = request.json
    dni = data.get('dni')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    telefono = data.get('telefono')
    ocupacion = data.get('ocupacion')

    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "INSERT INTO empleados (dni, nombre, apellido, telefono, ocupacion) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (dni, nombre, apellido, telefono, ocupacion))
        conn.commit()
        return jsonify({'message': f'Empleado {nombre} {apellido} agregado exitosamente.'}), 201
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Ruta para obtener empleados
@app.route('/ver_empleados', methods=['GET'])
def ver_empleados():
    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, dni, nombre, apellido, telefono, ocupacion FROM empleados")
        empleados = cursor.fetchall()
        return jsonify(empleados), 200
    except Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Ruta para agregar turno
@app.route('/agregar_turno', methods=['POST'])
def agregar_turno():
    data = request.json
    usuario_id = data.get('usuario_id')
    fecha = data.get('fecha')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')

    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "INSERT INTO turnos (usuario_id, fecha, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (usuario_id, fecha, hora_inicio, hora_fin))
        conn.commit()
        return jsonify({'message': 'Turno agregado exitosamente.'}), 201
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Ruta para obtener turnos
@app.route('/ver_turnos', methods=['GET'])
def ver_turnos():
    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute('''SELECT t.id, u.nombre, u.apellido, t.fecha, t.hora_inicio, t.hora_fin 
                          FROM turnos t JOIN usuarios u ON t.usuario_id = u.id''')
        
        turnos = cursor.fetchall()
        for turno in turnos:
            turno['fecha'] = turno['fecha'].strftime('%Y-%m-%d')  # Asegúrate de que fecha sea un objeto datetime
            
            # Convierto hora_inicio y hora_fin a un formato legible
            if isinstance(turno['hora_inicio'], timedelta):
                total_seconds = int(turno['hora_inicio'].total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                turno['hora_inicio'] = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                turno['hora_inicio'] = turno['hora_inicio'].strftime('%H:%M:%S')  # Asegúrate de que esto funcione
            if isinstance(turno['hora_fin'], timedelta):
                total_seconds = int(turno['hora_fin'].total_seconds())
                hours, remainder = divmod(total_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                turno['hora_fin'] = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                turno['hora_fin'] = turno['hora_fin'].strftime('%H:%M:%S')  # Asegúrate de que esto funcione

        return jsonify(turnos), 200
    except Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

# Funcionalidades para actualizar empleados y turnos
@app.route('/actualizar_empleado/<int:id>', methods=['PUT'])
def actualizar_empleado(id):
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    telefono = data.get('telefono')
    ocupacion = data.get('ocupacion')

    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "UPDATE empleados SET nombre=%s, apellido=%s, telefono=%s, ocupacion=%s WHERE id=%s"
        cursor.execute(query, (nombre, apellido, telefono, ocupacion, id))
        conn.commit()
        return jsonify({'message': 'Empleado actualizado exitosamente.'}), 200
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/actualizar_turno/<int:id>', methods=['PUT'])
def actualizar_turno(id):
    data = request.json
    fecha = data.get('fecha')
    hora_inicio = data.get('hora_inicio')
    hora_fin = data.get('hora_fin')

    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "UPDATE turnos SET fecha=%s, hora_inicio=%s, hora_fin=%s WHERE id=%s"
        cursor.execute(query, (fecha, hora_inicio, hora_fin, id))
        conn.commit()
        return jsonify({'message': 'Turno actualizado exitosamente.'}), 200
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Funcionalidades para eliminar empleados y turnos
@app.route('/eliminar_empleado/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "DELETE FROM empleados WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({'message': 'Empleado eliminado exitosamente.'}), 200
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/eliminar_turno/<int:id>', methods=['DELETE'])
def eliminar_turno(id):
    conn = conectar_db()
    if conn is None:
        return jsonify({'error': 'No se pudo conectar a la base de datos.'}), 500

    cursor = conn.cursor()
    try:
        query = "DELETE FROM turnos WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()
        return jsonify({'message': 'Turno eliminado exitosamente.'}), 200
    except Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

