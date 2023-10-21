import requests

url = 'http://localhost:5000/process-receit'
filename = '../samples/receit_1.jpg'

with open(filename, 'rb') as f:
    r = requests.post(url, files={'image': f})

print(r.status_code)