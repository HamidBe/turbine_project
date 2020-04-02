import json

from urllib.request import urlopen

myKey = "insert your server key here"
url = "https://gender-api.com/get?key=" + myKey + "&name=kevin"
url = "https://gender-api.com/get?name=elizabeth&key=UHpbZEfqcJwXBQzXwV"
response = urlopen(url)
decoded = response.read().decode('utf-8')
data = json.loads(decoded)
print( "Gender: " + data["gender"]); #Gender: male
