#Transforma el numero ingresado en su traduccion a letras normales

def contar_numero():
    
    try:
        numero = int(input("Ingresa un número (0-99): "))
        
    except ValueError:
        return "Entrada no válida. Ingresa un número entero."

    if numero < 0 or numero > 99:
        return "Número fuera de rango. Ingresa un número entre 0 y 99."
    
    texto_numeros = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }
    dos_cifras={10:"diez",11:"once",12:"doce",13:"trece",
                14:"catorce",15:"quince",16:"dieciseis",17:"diecisiete",
                18:"dieciocho",19:"diecinueve",20:"veinte"
    }
    decenas={2:"veinte y",3:"treinta y",4:"cuarenta y",5:"cincuenta y",
             6:"sesenta y",7:"setenta y",8:"ochenta y",9:"noventa y"
    }
    
    if numero<10:
        
        return texto_numeros[numero]
        
    if 10<=numero<=20:
    
        return dos_cifras[numero]
    
    if numero >20:
        decena=numero//10
        unidad=numero%10
        
        if unidad == 0:
            return decenas[decena]
        return f"{decenas[decena]} {texto_numeros[unidad]}"            
        

    
