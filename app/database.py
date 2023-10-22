import psycopg2
from .objects import *

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            port=5433,
                            database='mainDb',
                            user="wesoleJagodki",
                            password="forTheWin")
    return conn

def add_transaction(transaction: Transaction):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (user_id, amount, date, location, type, category) VALUES (%s, %s, %s, %s, %s, %s)", 
                (transaction.user_id, transaction.amount, transaction.date,
                 transaction.location, transaction.transaction_type, transaction.category))
    conn.commit()
    conn.close()

def add_purchase(purchase: Purchase, transaction_id: int):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO purchases (transaction_id, date, category, store, name, figure, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                (transaction_id, purchase.date, purchase.category, purchase.store,
                 purchase.name, purchase.figure, purchase.amount))
    conn.commit()
    conn.close()

def add_notification(content: str, user_id: int):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO notifications (user_id, content, used_flag) VALUES (%s, %s, false)", 
                (user_id, content))
    conn.commit()
    conn.close()

def add_goal(goal: Goal):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("INSERT INTO goals (user_id, spent_money, category, max_money) VALUES (%s, %s, %s, %s)", 
                (goal.user_id, goal.spent_money, goal.category, goal.max_money))
    conn.commit()
    conn.close()

def update_goal(goal: Goal):
    conn = get_db_connection()

    cur = conn.cursor()
    cur.execute("UPDATE goals SET spent_money = %s WHERE goal_id = %s", 
                (goal.spent_money, goal.goal_id))
    conn.commit()
    conn.close()

def get_all_goals():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM goals")
    rows = cur.fetchall()
    conn.close()
    
    objects = []
    for row in rows:
        goal = Goal(row[1], row[2], row[3])
        goal.max_money = row[4]
        goal.goal_id = row[0]
        objects.append(goal)

    return objects

def get_all_transactions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()
    conn.close()
    
    objects = []
    for row in rows:
        transaction = Transaction(row[6], row[0], row[1], row[3], row[4], row[5])
        transaction.transaction_id = row[4]
        objects.append(transaction)

    return objects

def get_all_purchases(transaction_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM purchases WHERE transaction_id = %s", (transaction_id, ))
    rows = cur.fetchall()
    conn.close()
    
    objects = []
    for row in rows:
        purchase = Purchase(row[1], row[2], row[3], row[4], row[5], row[6])
        purchase.transaction_id = row[0]
        purchase.purchase_id = row[7]
        objects.append(purchase)

    return objects
