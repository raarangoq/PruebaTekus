
import pandas
from SQL.db_connection import Connector



class Descargador:

    query_ollas = """
    SELECT post.potkey, post.serial, post.cityid, cities.name as "CityName" FROM
    [DataTest].[dbo].[Pots] AS post LEFT JOIN [DataTest].[dbo].[Cities] AS cities
    ON post.cityid = cities.cityid
    """
    
    query_ciudades = """
    SELECT *
    FROM [DataTest].[dbo].[Cities]
    """
        

    def __init__(self):
        self.connector = Connector()


    def descargar_ollas(self):
        print("\nDescargando data de ollas")
        query_string = self.query_ollas
        data = self.connector.read_data(query_string)

        return data

    def descargar_ciudades(self):
        print("\nDescargando data de ciudades")
        query_string = self.query_ciudades
        data = self.connector.read_data(query_string)

        return data











