# TonyAPI.py
# IAE 101, Fall 2021
# Author: Phi Long Bui
import requests as re
# This method use to create an account for the new user.
# parameters
#    username    : The username of the user
#    acc_token : The token used for every account that got created


def createAccount(username, acc_token):
    url = 'https://pixe.la/v1/users'
    myobj = ({"token": acc_token,
              "username": username,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"})

    response = re.post(url, json=myobj)
    result = f'{response.json().get("message")} I will update every 24 hours, make sure to check them out'
    return result
# end of createAccount()

# set the token
# This method use to set the accounts token for the new user.
# parameters
#    username : The username of the user
#    newToke : The given token


def setToken(newToken="", username=""):
    url = 'https://pixe.la/v1/users/' + username
# end of setToken()

# delete the account

# This method use to delete the selected account
# parameters
#    username    : The username of the user
#    acc_token : The token used for every account that need deleting


def deleteAccount(username="", acc_token=""):
    delete_headers = {"X-USER-TOKEN": acc_token}
    url = 'https://pixe.la/v1/users/' + username
    delete = re.delete(url, headers=delete_headers)
    # data = response.json()
    result = f'{delete.json().get("message")} Your account is deleted'
    return result
# end of deleteAccount()

# Create a habit graph
# This method use to create a gragh for selected account
# parameters
#    username : The username of the user
#    acc_token : The token used for every account that need deleting
#    id : The id of the graph
#    name : Name of the graph
#    unit : Unit used for the graph
#    timezone : The timezone used for the graph


def createGraph(username="", acc_token="", id="test-graph", name="graph-name", unit="commit", timezone="EST"):
    url = 'https://pixe.la/v1/users/' + username + '/graphs'
    header = {"X-USER-TOKEN": acc_token}
    obj = {"id": id,
           "name": name,
           "unit": unit,
           "type": "int",
           "color": "shibafu",
           "timezone": timezone,
           "isSecret": True,
           "publishOptionalData": True}
    graph = re.post(url, headers=header, json=obj)
    result = f'{graph.json().get("message")} Your {name} graph was created. You can find the graph at https://pixe.la/v1/users/{username}/graphs/{id}.html?mode=simple'
    return result
# end of createGraph()

# This method use to delete a gragh for selected account
# parameters
#    username : The username of the user
#    acc_token : The token used for every account that need deleting
#    id : The id of the graph


def deleteGraph(username="", acc_token="", id="test_graph"):
    url = f'https://pixe.la/v1/users/{username}/graphs/{id}'
    header = {"X-USER-TOKEN": acc_token}
    delete = re.delete(url, headers=header)
    result = f'{delete.json().get("message")} Your graph is deleted'
    return result
# end of deleteGraph()

# This method use to update the graph with one pixel a gragh for selected account
# parameters
#    date : The current date the pixel is added
#    username : The username of the user
#    acc_token : The token used for every account that need deleting
#    graphID : The id of the graph
#    quantity : The quality of the amount of <unit> that need to add into the pixel


def postPixel(date="20211204", username="", acc_token="", graphID="", quality="1"):
    url = 'https://pixe.la/v1/users/'+username+'/graphs/'+graphID
    header2 = {"X-USER-TOKEN": acc_token}
    obj = {"date": date,
           "quality": quality}
    pixel = re.post(url, headers=header2, json=obj)
    result = f'{pixel.json().get("message")} You have posted a pixel to your {graphID} graph. View your graph at https://pixe.la/v1/users/{username}/graphs/{graphID}.html?mode=simple'
    return result
# end of postPixel()
