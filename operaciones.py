class Operaciones:
    
    def sumarBinarios(self, bin1, bin2):
        bin1 = bin1.zfill(8)                                        ### Agrega ceros a la izquierda si es necesario, asegura que el número sea de 8 bits.
        bin2 = bin2.zfill(8)
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        resultadoDecimal = num1 + num2
        resultadoDecimal = resultadoDecimal % 256                 ### Asegura que el resultado no exceda los 8 bits
        resultadoBinario = bin(resultadoDecimal)[2:].zfill(8)
        return resultadoBinario

    def restarBinarios(self, bin1, bin2):
        bin1 = bin1.zfill(8)
        bin2 = bin2.zfill(8)
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        resultadoDecimal = num1 - num2
        resultadoDecimal = resultadoDecimal % 256
        resultadoBinario = bin(resultadoDecimal)[2:].zfill(8)
        return resultadoBinario
    
    def multiplicarBinarios(self, bin1, bin2):
        bin1 = bin1.zfill(8)
        bin2 = bin2.zfill(8)
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        resultadoDecimal = num1 * num2
        resultadoDecimal = resultadoDecimal % 256
        resultadoBinario = bin(resultadoDecimal)[2:].zfill(8)
        return resultadoBinario

    def exponenteBinarios(self, binNum, binExp):
        binNum = binNum.zfill(8)
        binExp = binExp.zfill(8)
        num = int(binNum, 2)
        exponente = int(binExp, 2)
        resultadoDecimal = num ** exponente
        resultadoDecimal = resultadoDecimal % 256
        resultadoBinario = bin(resultadoDecimal)[2:].zfill(8)
        return resultadoBinario
