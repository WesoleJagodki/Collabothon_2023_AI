"""
This should be some sort of AI in the future.
"""

def get_product_category(purchase_store: str):
    if purchase_store == "Good Restaurant":
        return "food"
    
    if purchase_store == "Biedronka":
        return "food"
    
    if purchase_store == "Lidl":
        return "food"
    
    if purchase_store == "Home Depot":
        return "home"
    
    return "other"

def get_transaction_cathegory(transaction):
    return get_product_category(transaction.location)
