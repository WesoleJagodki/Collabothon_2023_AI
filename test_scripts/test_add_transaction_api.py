import requests
import time

url = 'http://localhost:5000/add-transaction'

data = {"user_id": 7,
       "location": "pornhub",
       "amount": 100.0,
       "transaction_type": "card",
       "date": int(time.time())}

response = requests.post(url, json=data)

print(response.status_code)