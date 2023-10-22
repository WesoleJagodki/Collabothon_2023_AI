import time
from .database import *
from .objects import *
from .categories import get_product_category
from typing import List

def save_float(x):
    try :
        x = float(x)
    except ValueError as _:
        return float("nan")
    return x

def match_purchase_to_transaction(transactions: List[Transaction], date: int, store: str) -> Transaction:
    # Find transactions with the same store and within 1h of the same date.
    for transaction in transactions:
        if transaction.location == store and abs(transaction.date - date) < 120*60:
            return transaction
        
def update_goals(transaction: Transaction):
    goals = get_all_goals()
    for goal in goals:
        if goal.category == transaction.category:
            goal.spent_money += transaction.amount
            if goal.spent_money > goal.max_money:
                add_notification("You have exceeded your budget for category " + goal.category, goal.user_id)
            update_goal(goal)

def process_receit_from_img(user_id, basic_info, product_list):
    timestamp = int(time.time())
    store = basic_info['purchase_location']
    transaction = match_purchase_to_transaction(get_all_transactions(), timestamp, store)

    if transaction is None:
        transaction = Transaction(user_id=user_id, location=store, amount=save_float(basic_info['total_price_tag']),
                                  category=get_product_category(store),
                                  transaction_type="cash", date=timestamp)
        add_transaction(transaction)

        update_goals(transaction)

        # LOL this is horrible
        transaction = match_purchase_to_transaction(get_all_transactions(), timestamp, store)

    # Add purchases to transaction.
    for product in product_list:
        purchase = Purchase(category = get_product_category(store),
                            date=timestamp, store=store,
                            name=product['product_name'], figure=product['product_price'], amount=save_float(product['product_quantity']))
        
        add_purchase(purchase, transaction.transaction_id)

def process_api_transaction(request):
    transaction = Transaction(user_id=request['user_id'],
                              location=request['location'],
                              category=get_product_category(request['location']),
                              amount=save_float(request['amount']),
                              transaction_type=request['transaction_type'],
                              date= request['date'])
    add_transaction(transaction)
    update_goals(transaction)
 