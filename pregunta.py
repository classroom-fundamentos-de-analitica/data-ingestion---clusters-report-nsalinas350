"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    # Leer el archivo
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Listas para almacenar los datos de cada columna
    cluster_list = []
    cantidad_list = []
    porcentaje_list = []
    palabras_clave_list = []

    # Auxiliares para construir una línea completa
    current_line = ''
    is_complete_line = False
    lineNumber = 1

    # Iterar sobre las líneas del archivo
    for line in lines:

        if lineNumber >= 5:
            # Limpiar la línea de espacios en blanco al principio y al final
            line = line.strip()

            # Verificar si la línea está vacía
            if not line:
                # Verificar si se completó una línea antes de la línea en blanco
                if is_complete_line:
                    # Separar por espacios en blanco
                    elements = current_line.strip().split()

                    # Obtener los valores de cada columna
                    cluster = elements[0]
                    cantidad = elements[1]
                    porcentaje = elements[2].replace(',', '.')
                    palabras_clave = ' '.join(elements[4:]).replace('.', '')

                    # Agregar los valores a las listas
                    cluster_list.append(cluster)
                    cantidad_list.append(cantidad)
                    porcentaje_list.append(porcentaje)
                    palabras_clave_list.append(palabras_clave)

                # Reiniciar la línea actual para la siguiente iteración
                current_line = ''
                is_complete_line = False
                continue

            # Construir la línea completa juntando las líneas parciales
            current_line += line + ' '
            is_complete_line = True
        
        lineNumber += 1

    # Crear el dataframe de Pandas
    data = {
        'cluster': cluster_list,
        'cantidad_de_palabras_clave': cantidad_list,
        'porcentaje_de_palabras_clave': porcentaje_list,
        'principales_palabras_clave': palabras_clave_list
    }

    df = pd.DataFrame(data)
    df['cantidad_de_palabras_clave'] = pd.to_numeric(df['cantidad_de_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = pd.to_numeric(df['porcentaje_de_palabras_clave'])
    df['cluster'] = pd.to_numeric(df['cluster'])

    return df
