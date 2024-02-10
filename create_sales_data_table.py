import psycopg2

hostname = '127.0.0.1'
user='mike'        
pwd ='-----'      
port ="5432"                
database ="postgres"

conn = psycopg2.connect(
    database=database,
    user=user,
    password=pwd,
    host=hostname,
    port=port)

cursor = conn.cursor()

SQL = """CREATE TABLE sales_data (
    rowid INTEGER PRIMARY KEY,
    product_id INT,
    customer_id INT,
    price NUMERIC,
    quantity INT,
    timestamp TIMESTAMP
    )"""

cursor.execute(SQL)

print("Table Created")

conn.commit()