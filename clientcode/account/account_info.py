import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/account/info'
    headers = variable.headers
    data = {}

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
