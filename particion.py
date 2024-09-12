from operaciones import Operaciones
from funciones import Funciones

operaciones = Operaciones()
funciones = Funciones()

def obtenerPrimeros4Bits(numBinario):
    # Asegurarse de que el número binario sea de 8 bits
    numBinario = numBinario.zfill(8)
    
    # Obtener los primeros 4 bits
    primeros4 = numBinario[:4]
    
    return primeros4

def obtenerUltimos4Bits(numBinario):
    # Asegurarse de que el número binario sea de 8 bits
    numBinario = numBinario.zfill(8)
    
    # Obtener los últimos 4 bits
    ultimos4 = numBinario[-4:]
    
    return ultimos4

def codificacarOperacion(numBinario, num1, num2):
    operacion = obtenerPrimeros4Bits(numBinario)
    if operacion == "0000":
        valorResultado = operaciones.sumarBinarios(num1, num2)
    elif operacion == "0001":
        valorResultado = operaciones.restarBinarios(num1, num2)
    elif operacion == "0010":
        valorResultado = operaciones.multiplicarBinarios(num1, num2)
    elif operacion == "0011":
        valorResultado = operaciones.exponenteBinarios(num1, num2)     
        
    return valorResultado
