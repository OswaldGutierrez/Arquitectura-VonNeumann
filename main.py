import tkinter as tk
import subprocess

def abrirCalculadora():
    # Ejecutar el archivo principal.py
    subprocess.Popen(["python", "principal.py"])
    # Deshabilitar el botón para que solo se pueda hacer clic una vez
    botonRealizarOperacion.config(state=tk.DISABLED)

# Configuración básica de la ventana principal
root = tk.Tk()
root.title("Interfaz Principal")

# Hacer que la ventana sea responsiva
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Configuración del marco principal
frame = tk.Frame(root, bg="#F0F8FF", padx=20, pady=20)
frame.grid(sticky="nsew")

# Mostrar la operación (8-3)^3 en grande
labelOperacion = tk.Label(frame, text="(8-3)^3", font=("Helvetica", 36), bg="#F0F8FF")
labelOperacion.pack(pady=20)

# Botón para realizar la operación aritmética
botonRealizarOperacion = tk.Button(frame, text="Realizar Operación Aritmética", command=abrirCalculadora, font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonRealizarOperacion.pack(pady=20)

# Crear un marco para la tabla de información de instrucciones
tablaFrame = tk.Frame(frame, bg="#F0F8FF", pady=20)
tablaFrame.pack(pady=20)

# Añadir los encabezados de la tabla
encabezados = ["Inst", "D", "Comentario"]
for i, encabezado in enumerate(encabezados):
    labelEncabezado = tk.Label(tablaFrame, text=encabezado, font=("Helvetica", 12, "bold"), bg="#F0F8FF", borderwidth=1, relief="solid", padx=10, pady=5)
    labelEncabezado.grid(row=0, column=i, sticky="nsew")

# Añadir las filas de la tabla
instrucciones = [
    ("0000", "+", "Suma"),
    ("0001", "-", "Resta"),
    ("0010", "*", "Producto"),
    ("0011", "^", "Exponente"),
    ("0100", "&", "Operador AND"),
    ("0101", "|", "Operador OR"),
    ("0110", "M", "Mover a memoria"),
    ("0111", "…", "Finalizar"),
]

for i, (inst, d, comentario) in enumerate(instrucciones, start=1):
    labelInst = tk.Label(tablaFrame, text=inst, font=("Helvetica", 12), bg="#F0F8FF", borderwidth=1, relief="solid", padx=10, pady=5)
    labelInst.grid(row=i, column=0, sticky="nsew")
    
    labelD = tk.Label(tablaFrame, text=d, font=("Helvetica", 12), bg="#F0F8FF", borderwidth=1, relief="solid", padx=10, pady=5)
    labelD.grid(row=i, column=1, sticky="nsew")
    
    labelComentario = tk.Label(tablaFrame, text=comentario, font=("Helvetica", 12), bg="#F0F8FF", borderwidth=1, relief="solid", padx=10, pady=5)
    labelComentario.grid(row=i, column=2, sticky="nsew")

# Ajustar el tamaño mínimo de la ventana
root.minsize(400, 200)

# Loop principal de la aplicación
root.mainloop()
