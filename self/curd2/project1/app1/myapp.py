import requests
import json

URL="http://127.0.0.1:8000/stu_details/"

def get_data(id=None):
    data = {}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r= requests.get(url=URL, data=json_data)
    data=r.json()
    print(data)

#get_data(2)   

def post_data():
    data={
        
        'name':'Chani',
        'roll':104,
        'city':'Pune'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

#post_data()    

def post_data():
    data={
        'id':4,    
        'name':'Surbhi',
        'city':'Delhi'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#post_data()

def delete_data():
    data={'id':4}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

delete_data()