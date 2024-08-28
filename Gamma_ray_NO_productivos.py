import pandas as pd
import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random

#### Funciones para generar rangos y conjuntos ####
def generar_rango_0a60():
    num1 = random.randint(40, 60)  #### Asegura un rango válido ####
    num2 = num1 + 10
    if num2 > 60:
        num2 = 60
    return (num1, num2)

def generar_rango_60a140():
    num1 = random.randint(60, 120)  #### Asegura un rango válido ####
    num2 = num1 + 10
    if num2 > 140:
        num2 = 120
    return (num1, num2)

#### Parámetros ####
num_rows = 100  #### Cantidad de datos ####
set_size = num_rows // 10
folder_path = 'C:/Users/USER/Desktop/Aplicacion/GR_no_productivos/'
file_prefix = 'no_productivos_'

#### Asegurarse de que el directorio exista ####
os.makedirs(folder_path, exist_ok=True)

#### Obtener el número más alto de archivo existente ####
existing_files = [f for f in os.listdir(folder_path) if f.startswith(file_prefix) and f.endswith('.csv')]
numbers = [int(f.split('_')[-1].split('.')[0]) for f in existing_files if f.split('_')[-1].split('.')[0].isdigit()]
next_number = max(numbers, default=0) + 1

#### Generar 10 archivos CSV y gráficos ####
for i in range(10):
    #### Rangos menores a 60 ####
    rango_menor = generar_rango_0a60()
    rango_3 = rango_menor[0]
    rango_4 = rango_menor[1]
    #### Rangos mayores a 60 ####
    rango = generar_rango_60a140()
    rango_1 = rango[0]
    rango_2 = rango[1]
    
    #### Conjuntos menores a 60 ####
    set1 = np.sort(np.random.uniform(rango_1, rango_2 + 1, set_size))
    set2 = np.sort(np.random.uniform(rango_1, rango_2 + 1, set_size))[::-1]
    set3 = np.sort(np.random.uniform(rango_1, rango_2 + 1, set_size))
    set4 = np.sort(np.random.uniform(rango_1, rango_2 + 1, set_size))[::-1]
    set_total_1 = np.concatenate([set2, set1])
    set_total_2 = np.concatenate([set4, set3])
    
    #### Generar datos aleatorios en el rango ####
    rand1 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand2 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand3 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand4 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand5 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand6 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand7 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)
    rand8 = np.random.choice(np.arange(rango_1, rango_2 + 1), size=set_size, replace=True)

    #### Concatenar todos los conjuntos de datos ####
    all_sets = np.concatenate([set_total_1, rand1, rand2, set_total_2, rand3, rand4, rand5, rand6, rand7, rand8])

    #### Crear DataFrame ####
    df = pd.DataFrame(all_sets, columns=['Valor'])

    #### Generar el nombre del archivo CSV ####
    file_name = f'{file_prefix}_{next_number:02}.csv'  #### Cambiado a {next_number:02} para nombres consistentes con dos dígitos ####
    file_path = os.path.join(folder_path, file_name)
    df.to_csv(file_path, index=False)

    #### confirmacion de csv ####
    print(f"Archivo CSV generado exitosamente: {file_name}")

    #### Graficar los datos ####
    plt.figure(figsize=(20, 8))
    plt.plot(df['Valor'], color='#008202', linewidth=2)  #### Línea verde ####
    plt.title('Gráfico de Línea Verde de Gamma Ray')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    
    plt.ylim(0, 140)
    plt.gca().invert_yaxis()
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(base=200))
    plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(base=50))

    #### Guardar archivo temporal del gráfico ####
    temp_plot_file_path = os.path.join(folder_path, f'temp_plot_{next_number:02}.png')
    plt.savefig(temp_plot_file_path)
    plt.close()

    #### Rotar y guardar el gráfico ####
    image = Image.open(temp_plot_file_path)
    rotated_image = image.rotate(90, expand=True)
    plot_file_name = f'{file_prefix}_plot_{next_number:02}.png'
    plot_file_path = os.path.join(folder_path, plot_file_name)
    rotated_image.save(plot_file_path)

    #### Eliminar el archivo temporal ####
    os.remove(temp_plot_file_path)

    print(f"Gráfico rotado guardado exitosamente: {plot_file_name}")

    #### Incrementar el número para el siguiente archivo ####
    next_number += 1

    #### Mostrar la imagen rotada (opcional para revisión de datos) 
    rotated_image.show()
