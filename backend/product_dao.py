from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ('SELECT products.product_id, products.name, products.unit_of_measurement_id, products.price_per_unit, unit_of_measurement.name FROM grocery_store.products inner join grocery_store.unit_of_measurement ON products.unit_of_measurement_id = unit_of_measurement.unit_of_measurement_id')
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

if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_products(connection))