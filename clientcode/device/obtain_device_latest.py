import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/device/latest'
    headers = variable.headers

    """
    Fetch latest data of devices, supporting querying in batch, up to 10 devices per batch
    """
    data = {
        "deviceList": [
            "333333"    # Replace with your deviceSn
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
