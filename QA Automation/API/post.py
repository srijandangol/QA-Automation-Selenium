import requests
import json
#base url
base_url = 'https://reqres.in/api'
#auth tiken
auth_token = 'Token ... Token Value'

def post_request():
    url = base_url + "/users"
    print("post url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "RAM",
        "email": "Ram@gmail.com",
        "job": "QA Learner",
        "level": "Bachelor"
    }
    response = requests.post(url, json= data, headers= headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body:", json_str)
    user_id = json_data['id']
    print('User is ==>', user_id)
    assert response.status_code == 201
    print('......Get User is done.......')
    print('..........-------------.........')
    return user_id

user_id = post_request()