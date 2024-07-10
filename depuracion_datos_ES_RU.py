with open("palabras_espanol.txt","r",encoding="UTF-8") as file:
    palabras=file.readlines()
#print(palabras)

datos=[]

for dato in palabras:
    if  dato.strip():
        aux=dato.strip().split("\n",0)
        datos.append(aux)

#Para convertir las listas de datos en cadenas.
datos_limpios = [" ".join(aux) for aux in datos]


with open("summary.txt","r",encoding="UTF-8") as file:
    palabras_ru=file.readlines()
#print(palabras)
datos_ru=[]

for dato in palabras_ru:
    if  dato.strip():
        aux=dato.strip().split("\n",0)
        datos_ru.append(aux)

#Para convertir las listas de datos en cadenas.
datos_rusos_limpios = [" ".join(aux) for aux in datos_ru]
