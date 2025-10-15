import mysql.connector

connection = mysql.connector.connect(user='root', password='ElongatedMango1103!', host='127.0.0.1',database='grocery_store')

cursor = connection.cursor()

query = 'SELECT * FROM grocery_store.products'

cursor.execute(query)

for (product_id,name,unit_of_measurement_id,price_per_unit) in cursor:
    print(product_id,name,unit_of_measurement_id,price_per_unit)

connection.close()