import requests
import json
import random
import string
#base url
base_url = 'https://reqres.in/api'
#auth tiken
auth_token = 'Token ... Token Value'

def generate_random_email():
    domain = 'test.com'
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

def put_request(user_id):
    url = base_url + f'/users/{user_id}'
    print("Put url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "RAM",
        "email": generate_random_email(),
        "job": "QA Learner",
        "level": "Bachelor"
    }
    response = requests.post(url, json= data, headers= headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json put response body:", json_str)
    user_id = json_data['id']
    print('User is ==>', user_id)
    assert response.status_code == 201
    print('......Put User is done.......')
    print('..........-------------.........')
    return user_id

#call put request
put_request(264)
