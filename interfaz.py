import tkinter as tk
from tkinter import messagebox
from usuario import agregar_usuario
from turno import agregar_turno, ver_turnos

def agregar_usuario_gui():
    nombre = entry_nombre.get()
    agregar_usuario(nombre)
    messagebox.showinfo("Información", f"Usuario {nombre} agregado.")

def agregar_turno_gui():
    usuario_id = entry_usuario_id.get()
    fecha = entry_fecha.get()
    hora_inicio = entry_hora_inicio.get()
    hora_fin = entry_hora_fin.get()
    agregar_turno(usuario_id, fecha, hora_inicio, hora_fin)
    messagebox.showinfo("Información", f"Turno agregado para el usuario ID {usuario_id}.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema Gestor de Turnos")

# Crear widgets
label_nombre = tk.Label(ventana, text="Nombre del Usuario:")
entry_nombre = tk.Entry(ventana)

label_usuario_id = tk.Label(ventana, text="ID del Usuario:")
entry_usuario_id = tk.Entry(ventana)

label_fecha = tk.Label(ventana, text="Fecha (YYYY-MM-DD):")
entry_fecha = tk.Entry(ventana)

label_hora_inicio = tk.Label(ventana, text="Hora de Inicio (HH:MM:SS):")
entry_hora_inicio = tk.Entry(ventana)

label_hora_fin = tk.Label(ventana, text="Hora de Fin (HH:MM:SS):")
entry_hora_fin = tk.Entry(ventana)

boton_agregar_usuario = tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario_gui)
boton_agregar_turno = tk.Button(ventana, text="Agregar Turno", command=agregar_turno_gui)
boton_ver_turnos = tk.Button(ventana, text="Ver Turnos", command=lambda: ver_turnos())

# Ubicar widgets
label_nombre.pack()
entry_nombre.pack()
boton_agregar_usuario.pack()

label_usuario_id.pack()
entry_usuario_id.pack()
label_fecha.pack()
entry_fecha.pack()
label_hora_inicio.pack()
entry_hora_inicio.pack()
label_hora_fin.pack()
entry_hora_fin.pack()
boton_agregar_turno.pack()
boton_ver_turnos.pack()

# Ejecutar la aplicación
ventana.mainloop()
