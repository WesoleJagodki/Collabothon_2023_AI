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
                (user_id, parameters["total_price_tag"], parameters["purchase_date"], parameters["purchase_location"], parameters["transaction_type"]))
    conn.commit()
    conn.close()
