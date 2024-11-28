from database import crear_db_y_tablas
from usuario import agregar_usuario
from turno import agregar_turno, ver_turnos, eliminar_turno

def menu():
    while True:
        print("\nSistema Gestor de Turnos")
        print("1. Agregar Usuario")
        print("2. Agregar Turno")
        print("3. Ver Turnos")
        print("4. Eliminar Turno")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            dni = input("Ingrese el DNI del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            apellido = input("Ingrese el apellido del usuario: ")
            telefono = input("Ingrese el teléfono del usuario: ")
            resultado = agregar_usuario(dni, nombre, apellido, telefono)
            print(resultado)  # Mensaje de confirmación o error
        elif  opcion == "2":
            usuario_id = int(input("Ingrese el ID del usuario: "))
            empleado_id = int(input("Ingrese el ID del empleado: "))  # Solicitar el ID del empleado
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            hora_inicio = input("Ingrese la hora de inicio (HH:MM:SS): ")
            hora_fin = input("Ingrese la hora de fin (HH:MM:SS): ")
            agregar_turno(usuario_id, empleado_id, fecha, hora_inicio, hora_fin)  # Pasar empleado_id
            print(f"Turno agregado para el usuario ID {usuario_id} con empleado ID {empleado_id} en {fecha}.")

        elif opcion == "3":
            ver_turnos()
        elif opcion == "4":
            turno_id = int(input("Ingrese el ID del turno a eliminar: "))
            resultado = eliminar_turno(turno_id)
            print(resultado)  # Mensaje de confirmación o error
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    crear_db_y_tablas()  # Crear la base de datos y tablas al iniciar
    menu()

