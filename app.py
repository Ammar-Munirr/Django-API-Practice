import requests
import json


url = 'http://127.0.0.1:8000/api/students/'

def get(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=url,data=json_data)
    print(r.json())
    
    
    
    
get(2)