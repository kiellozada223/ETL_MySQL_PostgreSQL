# Import libraries required for connecting to mysql
import mysql.connector
# Import libraries required for connecting to PostgreSql
import psycopg2
# Connect to MySQL
mysql_conn = mysql.connector.connect(user='root', password='----',host = 'localhost', database = 'sales')

mysql_cursor = mysql_conn.cursor()
# Connect to PostgreSql
postgre_conn = psycopg2.connect(host='localhost', user='mike', password='------', port='5432', database='postgres')

postgre_cursor = postgre_conn.cursor()

# Find out the last rowid from PostgreSql data warehouse
# The function get_last_row must return the last rowid of the table sales_data on PostgreSql.

def get_last_row_id(query):

	postgre_cursor.execute(query)
	results = postgre_cursor.fetchone()
	postgre_conn.commit()
	return results[0]
	
SQL = 'SELECT rowid FROM sales_data ORDER BY rowid DESC LIMIT 1;'
last_row_id = get_last_row_id(SQL)
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):

	query = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
	mysql_cursor.execute(query)
	results = mysql_cursor.fetchall()
	mysql_conn.commit()
	return results	

new_records = get_latest_records(last_row_id)


print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in PostgreSql.

def insert_records(records):
	
	for row in records:

		SQL = "INSERT INTO sales_data(rowid,product_id,customer_id,quantity) VALUES(%s,%s,%s,%s)"
		postgre_cursor.execute(SQL, row);
		postgre_conn.commit()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
mysql_conn.close()
# disconnect from PostgreSql data warehouse 
postgre_conn.close()
# End of program