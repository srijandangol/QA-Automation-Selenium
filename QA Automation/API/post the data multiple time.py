import random
import string
import time
import re

#base url
base_url = 'https:/reqres.in/api'
#auth_token
auth_token = 'token...token value'

def generate_random_email():
    domain = 'test.com'
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

def post_request():
    url=base_url + "/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}