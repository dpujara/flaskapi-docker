import requests 
url = "http://192.168.99.100:5000/"
r = requests.get(url = url)
print(r.json())
r = requests.post(url = url)
print(r.json())