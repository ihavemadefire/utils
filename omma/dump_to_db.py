import pandas as pd
from sqlalchemy import create_engine
import pymysql

user = 'root'
password = '<password>'
host = 'localhost'
port = 3306
database = 'omma'
 
mydb =create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
df = pd.read_csv('table.csv')
df.to_sql('dispensaries', con=mydb, if_exists='replace', index=False)