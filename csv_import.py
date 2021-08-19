import pandas as pd
import mysql.connector
from mysql.connector import Error
empdata = pd.read_csv('output.csv', index_col=False, delimiter = ',')
empdata.head()
#print(empdata)


try:
    conn = mysql.connector.connect(host='localhost',
        database='doreme_eshop',user='root',password='')
    if conn.is_connected():
        cursor = conn.cursor()
        
        sql = "TRUNCATE TABLE doreme_order_master"
        cursor.execute(sql)
        #loop through the data frame
        conn.commit()
        for i,row in empdata.iterrows():
            #print(row['order_Date'])
            #here %S means string values 
            sql = "INSERT INTO doreme_order_master VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)