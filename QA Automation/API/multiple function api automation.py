import requests
import random
import string
import json

# Base URL
base_url = 'https://reqres.in/api'
# Auth token
auth_token = 'Token ... Token Value'  # Replace with your actual token

def generate_random_email():
    domain = 'test.com'
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

def generate_random_first_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_random_last_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

def generate_random_phone():
    return '+977-98' + ''.join(random.choice(string.digits) for _ in range(8))

def generate_random_message():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=80))

# Post request
def post_request():
    url = base_url + "/users"
    print("Post URL: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "first_name": generate_random_first_name(),
        "last_name": generate_random_last_name(),
        "email": generate_random_email(),
        "contact_number": generate_random_phone(),
        "message": generate_random_message()
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("JSON Post Response Body:", json_str)
    user_id = json_data['id']
    print('User ID is ==>', user_id)
    assert response.status_code == 201
    print('......Post/Create User is done.......')
    print('..........-------------.........')
    return user_id

for _ in range(10):
    user_id = post_request()
