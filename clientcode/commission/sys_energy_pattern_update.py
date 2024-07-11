import requests
from clientcode import variable

# Set energy pattern as BATTERY_FIRST or LOAD_FIRST
if __name__ == '__main__':
    url = variable.baseurl + '/order/sys/energyPattern/update'
    headers = variable.headers
    data = {
        "deviceSn": "000000",
        "energyPattern": "BATTERY_FIRST"        # options:BATTERY_FIRST;LOAD_FIRST
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
