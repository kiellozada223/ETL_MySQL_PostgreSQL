# ETL_MySQL_PostgreSQL
This project is about data synchronized between different databases/data warehouses. The task is to routinely performed is the sync up of staging data warehouse and production data warehouse. Automating this sync up will save you a lot of time and standardize your process. Perform the incremental data load from MySQL server which acts as a staging warehouse to PostgreSQL which is a production data warehouse. The script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse.

# Objectives
### Connect to PostgreSQL data warehouse and identify the last row on it.
### Connect to MySQL staging data warehouse and find all rows later than the last row on the datawarehouse.
### Insert the new data in the MySQL staging data warehouse to PostgreSQL production data warehouse.

# Tools
### VSCode
### MySQL
### pgAdmin 4
