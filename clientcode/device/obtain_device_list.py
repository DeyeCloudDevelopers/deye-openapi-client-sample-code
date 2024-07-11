import requests
from clientcode import variable


# Fetch device list for business members
if __name__ == '__main__':
    url = variable.baseurl + '/device/list'
    headers = variable.headers
    data = {
        "page": 1,
        "size": 20
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
