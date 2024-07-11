import requests
from clientcode import variable

# Enable or disable solar sell
if __name__ == '__main__':
    url = variable.baseurl + '/order/sys/solarSell/control'
    headers = variable.headers
    data = {
        "action": "off",            # Enable: action=on; Disable: action=off
        "deviceSn": "000000"
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())
