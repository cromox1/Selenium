__author__ = 'cromox'

#import pandas as pd
#import pandas.io.sql as psql



#query = "select * from rosli1;"
#para
#frm = pd.read_sql(query, )
#
#print(query % bind_params)


import pyodbc

import pandas.io.sql as psql

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=mengkome.mysql.pythonanywhere-services.com;DATABASE=mengkome$roslimainone;UID=mengkome;PWD=qwerty123456')
cursor = cnxn.cursor()
sql = ("""select * from rosli1""")

df = psql.frame_query(sql, cnxn)
cnxn.close()
