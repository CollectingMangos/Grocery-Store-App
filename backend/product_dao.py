import mysql.connector

connection = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='grocery_store')

cursor = connection.cursor()

query = ('SELECT products.product_id, products.name, products.unit_of_measurement_id, products.price_per_unit, unit_of_measurement.name FROM grocery_store.products inner join grocery_store.unit_of_measurement ON products.unit_of_measurement_id = unit_of_measurement.unit_of_measurement_id')

cursor.execute(query)

for (product_id,name,unit_of_measurement_id,price_per_unit, name) in cursor:
    print(product_id,name,unit_of_measurement_id,price_per_unit,name)

connection.close()