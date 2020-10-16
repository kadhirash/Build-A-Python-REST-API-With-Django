import json
import requests  # http requests


BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"


def get_list(id=None):
    data = None
    if not id:
        data = json.dumps({"id": id})

    r = requests.get(BASE_URL + ENDPOINT, data=data)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:  # Error
        print("Not good sign?")
    data = r.json()
    return data
#print(get_list())

def create_update():
    new_data = {"user": 1, "content": "Some more cool content"}
    r = requests.post(BASE_URL + ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text


#print(create_update())


def do_obj_update():
    new_data = {"id": 28, "user": 1, "content": "Testing this update"}
    r = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    # new_data = {"id":1, "content": "Some more cool content"}
    # r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.status_code)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text
#print(do_obj_update())

def do_obj_delete():
    new_data = {"id": 28}
    r = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    # new_data = {"id":1, "content": "Some more cool content"}
    # r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.status_code)
    # print(r.headers)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

print(do_obj_delete())

