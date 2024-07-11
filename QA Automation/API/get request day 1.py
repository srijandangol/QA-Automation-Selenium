import requests
import json

#base url
base_url='https://reqres.in/api'

#auth_token
auth_token='token...token value'

def get_request():
    url=base_url + '/users'
    print('get url:' + url)
    headers = {'Authorization': auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent = 4)
    print('json Get response body:' , json_str)
    print('......Get user is finish...........')
    print('.......=============...............')

#call
get_request()