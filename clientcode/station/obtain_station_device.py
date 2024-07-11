import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/station/device'
    headers = variable.headers
    data = {
        "page": 1,
        "size": 10,
        "stationIds": [10]    # Replace with your station ids
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
