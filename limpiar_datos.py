# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:23:15 2021

@author: asus
"""


import pandas as pd


from SQL.descarga import Descargador


descarga = Descargador()

ollas = descarga.descargar_ollas()
ciudades = descarga.descargar_ciudades()





