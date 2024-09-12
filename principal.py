import tkinter as tk
import particion
from contBinario import ContadorBinario  # Asegúrate de que la ruta sea correcta
from operaciones import Operaciones
from funciones import Funciones


# Datos iniciales
tablaDeMemoria = {
    "0000" : "00000101",
    "0001" : "00010110",
    "0010" : "00110110",
    "0011" : "01100111",
    "0100" : "01110000",
    "0101" : "00001000",
    "0110" : "00000011",
    "0111" : "00000000",
}


# Dicc con las instrucciones y sus significados
intruccionData = {
    "0000" : "+",
    "0001" : "-",
    "0010" : "*",
    "0011" : "^",
    "0100" : "&",
    "0101" : "|",
    "0110" : "M",
    "0111" : "...",
}

# Crear una instancia del contador binario
contador = ContadorBinario()
operaciones = Operaciones()
funciones = Funciones()

# Variables globales
clickContador = 0

def actualizarTablaMemoria():
    memoryTable.config(state=tk.NORMAL)  # Habilitar edición temporalmente para actualizar texto
    memoryTable.delete(1.0, tk.END)  # Limpiar el contenido actual

    # Encabezado de la tabla
    memoryTable.insert(tk.END, 
        "Dir    | Contenido\n"
        "--------------------\n"
    )
    # Insertar cada par clave-valor del diccionario en la tabla
    for direccion, contenido in tablaDeMemoria.items():
        memoryTable.insert(tk.END, f"{direccion}   | {contenido}\n")

    memoryTable.config(state=tk.DISABLED)  # Deshabilitar edición para mostrar solo información


def siguientePaso():
    global clickContador

    clickContador += 1  # Incrementar el número de clics

    if clickContador == 1:
        # Paso 1: Mostrar el valor de contPrograma
        valorContador = contador.contador
        contPrograma.config(text=valorContador)
        
    elif clickContador == 2:
        valorContador = contador.contador
        rDirecciones.config(text=valorContador)
        
    elif clickContador == 3:
        valorContador = contador.incrementar()
        contPrograma.config(text=valorContador)

    elif clickContador == 4:
        # Paso 2: Actualizar rDatos con el valor del diccionario memory_data
        direccionTabla = rDirecciones.cget("text")  # Obtener el texto actual de rDirecciones
        valorDato = tablaDeMemoria.get(direccionTabla, "No encontrado")  # Buscar el valor en el diccionario
        rDatos.config(text=valorDato)  # Actualizar rDatos con el valor encontrado

    elif clickContador == 5:
        # Paso 3: Actualizar rInstrucciones con el valor de rDatos
        valorRegistroDatos = rDatos.cget("text")  # Obtener el texto actual de rDatos
        rInstrucciones.config(text=valorRegistroDatos)  # Actualizar rInstrucciones con el valor de rDatos
        
    elif clickContador == 6:
        # Paso 4: Actualizar decodificador con los primeros 4 bits de rInstrucciones
        valorRegistroIntrucciones = rInstrucciones.cget("text")
        valorDecodificador = particion.obtenerPrimeros4Bits(valorRegistroIntrucciones)
        signoDecodificador = intruccionData.get(valorDecodificador)
        decodificador.config(text=signoDecodificador)
        
        # Verificar si el valor del decodificador es 'F' y deshabilitar el botón si es así
        if signoDecodificador == "...":
            botonSiguiente.config(state=tk.DISABLED)
            return  # Detener la ejecución

    elif clickContador == 7:
        # Paso 5: Actualizar rDirecciones con los últimos 4 bits de rInstrucciones
        valorUltimoRegistroInstrucciones = rInstrucciones.cget("text")
        valor2Direcciones = particion.obtenerUltimos4Bits(valorUltimoRegistroInstrucciones)
        rDirecciones.config(text=valor2Direcciones)
        
    elif clickContador == 8:
        # Paso 6: Actualizar rDatos con el valor del diccionario memory_data
        instruccionRealizar = decodificador.cget("text")
        if instruccionRealizar != "M":
            direccionTabla = rDirecciones.cget("text")  # Obtener el texto actual de rDirecciones
            valorDato = tablaDeMemoria.get(direccionTabla, "No encontrado")  # Buscar el valor en el diccionario
            rDatos.config(text=valorDato)  # Actualizar rDatos con el valor encontrado
        else:
            valorAcum = acumulador.cget("text")
            rDatos.config(text=valorAcum)
            claveDiccionario = rDirecciones.cget("text")
            valorDiccionario = rDatos.cget("text")
            tablaDeMemoria[claveDiccionario] = valorDiccionario                 ## Agregar otro paso para que no actualice rDatos y el contenido de memoria al mismo tiempo
        
        
    elif clickContador == 9:
        # Paso 7: Actualizar rEntrada con el valor de rDatos
        instruccionRealizar = decodificador.cget("text")
        if instruccionRealizar != "M":  # Solo actualiza rEntrada si la operación no es M
            valorDato = rDatos.cget("text")
            rEntrada.config(text=valorDato)
        else:
            valorContador = contador.contador
            rDirecciones.config(text=valorContador)  # Opcional, si también quieres actualizar rDirecciones con el valor de contPrograma
            
            # Reiniciar el clickContador para repetir los pasos del 2 al 9
            clickContador = 2
        
        
    elif clickContador == 10:
        valorAcumulador = acumulador.cget("text")
        valorEntrada = rEntrada.cget("text")
        valorRegistroIntrucciones = rInstrucciones.cget("text")
        instruccionRealizar = particion.obtenerPrimeros4Bits(valorRegistroIntrucciones)
        
        valorResultado = particion.codificacarOperacion(valorRegistroIntrucciones, valorAcumulador, valorEntrada)
       
        if instruccionRealizar == "0110":
            valorClave = rDirecciones.cget("text")
            valorValor = acumulador.cget("text")
            valorResultado = funciones.actualizarMemoria(valorClave, valorValor)

        acumulador.config(text=valorResultado)
        
    elif clickContador == 11:
        # Paso 9: Incrementar el contador de programa
        #valorContador = contador.incrementar()  # Incrementar y obtener el nuevo valor
        #contPrograma.config(text=valorContador)
        valorContador = contador.contador
        rDirecciones.config(text=valorContador)  # Opcional, si también quieres actualizar rDirecciones con el valor de contPrograma
        
        # Reiniciar el clickContador para repetir los pasos del 2 al 9
        clickContador = 2

    print("Click número: ", clickContador)
    actualizarTablaMemoria()  # Actualizar componentes como ejemplo    


def reiniciarOperacion():
    global clickContador
    
    # Restablecer variables globales
    clickContador = 0
    contador.reset()  # Asumiendo que tienes un método reset() para reiniciar el contador
    contPrograma.config(text="")
    acumulador.config(text="")  # Valor inicial del acumulador
    rEntrada.config(text="")  # Valor inicial del registro de entrada
    rDatos.config(text="")  # Valor inicial del registro de datos
    rDirecciones.config(text="")  # Valor inicial del registro de direcciones
    rInstrucciones.config(text="")  # Valor inicial de las instrucciones
    decodificador.config(text="")  # Valor inicial del decodificador
    
    # Formatear la Tabla de Memoria
    tablaDeMemoria["0111"] = "00000000" 

    # Actualizar la tabla de memoria
    actualizarTablaMemoria()
    
    # Habilitar el botón "Siguiente" si estaba deshabilitado
    botonSiguiente.config(state=tk.NORMAL)
    
    

# Configuración básica de la ventana principal
root = tk.Tk()
root.title("Simulación de Arquitectura Von Neumann")

# Hacer que la ventana sea responsiva
root.rowconfigure(0, weight=1)
root.columnconfigure([0, 1, 2], weight=1)
root.rowconfigure(1, weight=1)

# Unidad de Control (parte superior izquierda)
frameControl = tk.Frame(root, bg="#87CEEB", bd=2, relief="groove", padx=10, pady=10)
frameControl.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frameControl, text="Unidad de Control").pack()

# Decodificador
tk.Label(frameControl, text="Decodificador").pack()
decodificador = tk.Label(frameControl, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
decodificador.pack()

# Contador de Programa
tk.Label(frameControl, text="Contador de Programa").pack()
contPrograma = tk.Label(frameControl, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
contPrograma.pack()

# Instrucciones
tk.Label(frameControl, text="Instrucciones").pack()
rInstrucciones = tk.Label(frameControl, bg="white", width=20, height=4, anchor="center", font=("Helvetica", 16))
rInstrucciones.pack()

# Unidad Aritmético-Lógica (parte superior derecha)
frameAlu = tk.Frame(root, bg="#98FB98", bd=2, relief="groove", padx=10, pady=10)
frameAlu.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
tk.Label(frameAlu, text="Unidad Aritmético-Lógica").pack()

# Acumulador
tk.Label(frameAlu, text="Acumulador").pack()
acumulador = tk.Label(frameAlu, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
acumulador.pack()

# Registro de Entrada
tk.Label(frameAlu, text="Registro de Entrada").pack()
rEntrada = tk.Label(frameAlu, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rEntrada.pack()

# Memoria (parte inferior)
frameMemory = tk.Frame(root, bg="#FFDAB9" , bd=2, relief="groove", padx=10, pady=10)
frameMemory.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
tk.Label(frameMemory, text="Memoria").pack()

# Registro de Direcciones (parte izquierda)
frameAddress = tk.Frame(frameMemory, bd=1, relief="sunken", padx=10, pady=10)
frameAddress.pack(side=tk.LEFT, fill=tk.Y)
tk.Label(frameAddress, text="Registro de Direcciones").pack()
rDirecciones = tk.Label(frameAddress, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rDirecciones.pack()

# Tabla de Memoria (parte inferior)
memoryTable = tk.Text(frameMemory, bg="white", width=40, height=10, wrap=tk.NONE)
memoryTable.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Registro de Datos (parte derecha)
frameData = tk.Frame(frameMemory, bd=1, relief="sunken", padx=10, pady=10)
frameData.pack(side=tk.RIGHT, fill=tk.Y)
tk.Label(frameData, text="Registro de Datos").pack()
rDatos = tk.Label(frameData, bg="white", width=20, height=2, anchor="center", font=("Helvetica", 16))
rDatos.pack()

# Inicializar la tabla de memoria
actualizarTablaMemoria()

# Botón "Siguiente" en la parte inferior
botonSiguiente = tk.Button(root, text="Siguiente", command=siguientePaso)
botonSiguiente.grid(row=2, column=0, columnspan=3, pady=10)

# Botón "Reiniciar"
botonReiniciar = tk.Button(root, text="Reiniciar", command=reiniciarOperacion)
botonReiniciar.grid(row=20, column=0, columnspan=3, pady=10)

# Loop principal de la aplicación
root.mainloop()