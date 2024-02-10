import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Acurarsx776787',database='sales')

cursor = conn.cursor()

def get_latest_records(query):

    cursor.execute(query)
    column_name = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    df = pd.DataFrame(results, columns=column_name)
    return print(df)

SQL = 'SELECT * FROM sales_data WHERE rowid > 12289;'
get_latest_records(SQL)
