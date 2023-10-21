import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            port=5433,
                            database='mainDb',
                            user="wesoleJagodki",
                            password="forTheWin")
    return conn

def add_transaction(parameters, user_id):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (user_id, amount, date, location, type) VALUES (%s, %s, %s, %s, %s)", 
                (user_id, parameters["total_price_tag"], parameters["purchase_date"],
                 parameters["purchase_location"], parameters["transaction_type"]))
    conn.commit()
    conn.close()

def add_purchase(parameters, transaction_id):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO purchases (transaction_id, date, category, store, name, figure, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (transaction_id, parameters["purchase_date"], parameters["category"], parameters["purchase_location"],
                 parameters["product_name"], parameters["product_price"], parameters["product_quantity"]))
    conn.commit()
    conn.close()
