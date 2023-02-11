import json
import requests


url= "http://127.0.0.1:8000/create/"
data = {

    'no':95,
    'name':'lucy',
    'address':'pine',
    'phone':8549
}
json_data = json.dumps(data)
r = requests.post(url=url, data=json_data)
data = r.json()
print(data)

URL='http://127.0.0.1:8000/create/'
# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     json_data=json.dumps(data)
#     resp=requests.get(URL,data=json_data)
#     data= resp.json()
#     print(data)
#     # print(resp.status_code)
#     # print(resp.json())
# get_resources()

# def create_resource():
#     new_stud={
#         'no':12,
#         'name':'pramod',
#         'address':'beed',
#         'phone': 564789
#     }
#     json_data=json.dumps(new_stud)
#     resp=requests.post(URL,data=json_data)
#