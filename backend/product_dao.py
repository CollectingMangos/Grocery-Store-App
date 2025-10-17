from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.unit_of_measurement_id, products.price_per_unit, unit_of_measurement.name FROM grocery_store.products inner join grocery_store.unit_of_measurement ON products.unit_of_measurement_id = unit_of_measurement.unit_of_measurement_id")
    cursor.execute(query)
    response = []
    for (product_id,product_name,unit_of_measurement_id,price_per_unit, name) in cursor:
        response.append({
                "product_id":product_id,
                "name":product_name,
                "uom_id":unit_of_measurement_id,
                "price_per_unit":price_per_unit,
                "uom_name": name,
            })
    return response

def insert_new_product(connection,product):
    cursor = connection.cursor()
    query = ("INSERT INTO grocery_store.products (name, unit_of_measurement_id, price_per_unit) VALUES (%s,%s,%s)")
    data = (product["name"],product["unit_of_measurement_id"],product["price_per_unit"])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM grocery_store.products WHERE product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()
    
    return cursor.lastrowid    

if __name__ == "__main__":
    connection = get_sql_connection()
    # print(insert_new_product(connection, {
    #     "name":"cabbage",
    #     "unit_of_measurement_id":1,
    #     "price_per_unit":"9.99"
    # }))
    # print(delete_product(connection,11))
    print(get_all_products(connection))