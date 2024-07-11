import requests
from clientcode import variable

# Fetch measure points according to deviceSn
if __name__ == '__main__':
    url = variable.baseurl + '/device/measurePoints'
    headers = variable.headers
    data = {
     "deviceSn": "000000"
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
