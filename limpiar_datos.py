# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:23:15 2021

@author: asus
"""


import pandas as pd
import glob
import os

from SQL.descarga import Descargador



"""
Descarga de datos de las ollas, alojados en un servidos SQL 

"""


# Lectura de datos SQL desde Python
descarga = Descargador()

info_ollas = descarga.descargar_ollas()
ciudades = descarga.descargar_ciudades()




info_ollas.to_excel('./clean data/ollas.xlsx', index=False)
ciudades.to_excel('./clean data/ciudades.xlsx', index=False)


"""
Lectura y consolidación de los datos en archivos CSV, datos de los movientos de las ollas
"""


# Iniciar lectura de datos en CSV
ruta_inicial = "raw data/data-engineer-sample-data-v2/"

movimientos = [] # Lista donde consolidar lo leido

# Listar todos los archivos primero
lista_archivos = []
# r=root, d=directories, f = files
for r, d, f in os.walk(ruta_inicial):
    for file in f:
        if file.endswith(".csv"):
            lista_archivos.append(os.path.join(r, file))

# Ir por cada archivo, leer lo necesario y agregar al dataframe "movimientos"
for file in lista_archivos:
    
    #file = lista_archivos[0]
    #file = file.replace('\\', '/').replace('//', '/')
    #_, _, id_olla, anho, mes, dia, hora = file.split('/')
    #hora = hora.split('.')[0].replace('-', ':')
    data = pd.read_csv(file, usecols=['Duration', 'MovementDuration', 'MovementInteractions',
                                      'HardwareInteractions', 'Key', 'Date'])
    #data['potkey'] = id_olla
    #data['fecha'] = anho + "/" + mes + "/" + dia + " " + hora 
    
    movimientos.append(data)


# Convertir la lista de dataframes que es "movimientos" en un único dataframe
# Así es un poco mas eficiente que pegar cada dato nuevo en un dataframe
movimientos = pd.concat(movimientos, ignore_index=True)

movimientos['Date'] = pd.to_datetime(movimientos['Date'].str.split('.').str[0].str.replace('T', ' '))


# Columna HardwareInteractions completamente estática en el valor 0, eliminar ??
# O no se usa nunca, o hay un fallo en la recolección de la información.
#print("Valores diferentes para la columna HardwareInteractions: ", 
#      movimientos['HardwareInteractions'].unique())
#movimientos.drop(['HardwareInteractions'], axis=1, inplace=True)

# Ver valores nulos
movimientos.isna().sum()
# No hay valores nulos

movimientos.to_excel('./clean data/movimientos.xlsx', index=False)













