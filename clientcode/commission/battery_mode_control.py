import requests
from clientcode import variable

# Set the value of battery-related parameter
if __name__ == '__main__':
    url = variable.baseurl + '/order/battery/modeControl'
    headers = variable.headers

    """
    Enable or disable the chargeMode
    """
    data = {
            "deviceSn": "000000",
            "batteryModeType": "GRID_CHARGE",
            "action": "on"
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
