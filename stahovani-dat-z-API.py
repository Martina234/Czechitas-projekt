import requests
import json
response = requests.get('http://api.kodim.cz/python-data/people')
#response = requests.get('http://seznam.cz')
data = json.loads(response.text)
print(data)