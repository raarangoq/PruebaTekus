

import pyodbc
import pandas


class Connector:

    connect_string = ""

    def __init__(self):
        """
        Read connection data and initialize connection string
        """
        
        details = {
         'server': "proyectos.tekus.co",  # connection_data.at[0, "server"],
         'database': "DataTest",
         'username': "datatest",
         'password': "9cUQ*48AAX8Q"
         }

        self.connect_string = 'DRIVER={{ODBC Driver 17 for SQL Server}};' \
                              'SERVER={server};' \
                              'PORT=1433; ' \
                              'DATABASE={database};' \
                              'UID={username};' \
                              'PWD={password}'.format(**details)

    def read_data(self, query_string):
        """
        Performs a query on the database, to read data only
        :param query_string: string with a sql query to read data
        :type query_string: str

        :return: DataFrame with data read
        :rtype: pandas.DataFrame
        """
        connection = pyodbc.connect(self.connect_string)
        df = pandas.read_sql(query_string, connection)

        connection.close()
        return df


