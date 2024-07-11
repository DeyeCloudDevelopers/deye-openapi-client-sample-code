import requests
from clientcode import variable

# Set the value for MAX_SELL_POWER or MAX_SOLAR_POWER
if __name__ == '__main__':
    url = variable.baseurl + '/order/sys/power/update'
    headers = variable.headers

    """
    powerType= MAX_SELL_POWER or MAX_SOLAR_POWER; value=the value you want to set
    """
    data = {
        "deviceSn": "000000",
        "powerType": "MAX_SELL_POWER",
        "value": 0
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
