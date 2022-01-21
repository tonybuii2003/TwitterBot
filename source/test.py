import requests as re
from requests.api import head
url = 'https://pixe.la/v1/users'
user = "tonybui"
user2 = "tonybui2004"
acc_token = "account01"
# myobj = ({"token": acc_token,
#           "username": user,
#           "agreeTermsOfService": "yes",
#           "notMinor": "yes"})
# response = re.post(url, json=myobj)
# # Update a user
# url2 = 'https://pixe.la/v1/users/' + user
# print(f'User name url: {url2}')
# headers_dict = {"X-USER-TOKEN": acc_token}
# # update_token = "update_" + acc_token
# update_obj = {"newToken": acc_token}
# update = re.put(url2, headers=headers_dict, json=update_obj)
# # url_graph =
# # graph = re.get('')

# # {"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}
# delete_headers = {"X-USER-TOKEN": "account02"}
# url3 = 'https://pixe.la/v1/users/' + user2
# delete = re.delete(url3, headers=delete_headers)
# # data = response.json()
# print(delete.text)

# url4 = 'https://pixe.la/v1/users/' + user + '/graphs'
# header = {"X-USER-TOKEN": acc_token}
# obj = {"id": "test-graph",
#        "name": "graph-name",
#        "unit": "commit",
#        "type": "int",
#        "color": "shibafu",
#        "timezone": "EST",
#        "isSecret": True,
#        "publishOptionalData": True}
# graph = re.post(url4, headers=header, json=obj)
# print(graph.text)

url5 = 'https://pixe.la/v1/users/'+user+'/graphs/test-graph'
header2 = {"X-USER-TOKEN": acc_token}
optionalKey = 'hours'
optionalValue = '5'
obj = {"date": "20211208",
       "quantity": "7",
       "optionalData": "{\"optionalKey\":\"optionalValue\"}"}
pixel = re.post(url5, headers=header2, json=obj)
result = (pixel.json().get('message'))
print(result)
