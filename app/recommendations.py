"""
Advanced pattern detection and recommendation engine for saving advices is impossible to do in 2 days
so we do hardcoded recommendations based on product name for demo.
"""
from .objects import *
from .database import *
from typing import List

BAD_PRODUCT_NAME = "BISCUITS"
RECOMMENDATION = "You can purchase product 'BISCUITS' cheaper in Biedronka"
USER_ID = 7

# Returns none if there is
def generate_recommendations(purchases: List[Purchase]):
    for purchase in purchases:
        if purchase.name == BAD_PRODUCT_NAME:
            return RECOMMENDATION
    return None

def on_new_data():
    # Get latest transaction.
    latest_transaction = get_all_transactions()[-1]
    purchase = get_all_purchases(latest_transaction.transaction_id)

    recommendation = generate_recommendations(purchase)
    if recommendation is not None:
        add_notification(recommendation, USER_ID)
