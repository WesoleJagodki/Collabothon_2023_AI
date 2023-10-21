import sys
sys.path.append("../")

from app.database import add_transaction

parameters = {
    "total_price_tag": 10.12,
    "purchase_date": "2023-10-21",
    "purchase_location": "Biedronka",
    "transaction_type": "card"
}

add_transaction(parameters, 1)
