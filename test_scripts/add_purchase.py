import sys
sys.path.append("../")

from app.database import add_purchase

parameters = {
"purchase_date": 121344155,
"category": "fun",
"purchase_location": "harry potter store",
"product_name": "harry potter book",
"product_price": 12.34,
"product_quantity": 2
}

add_purchase(parameters, 3)