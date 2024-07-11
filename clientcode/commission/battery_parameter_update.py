import requests
from clientcode import variable

# Set the value of battery-related parameter
if __name__ == '__main__':
    url = variable.baseurl + '/order/battery/parameter/update'
    headers = variable.headers

    """
    Set the value for MAX_CHARGE_CURRENT and MAX_DISCHARGE_CURRENT
    e.g.Field paramterType=MAX_CHARGE_CURRENT, Field value=the value you want to set
    """
    data = {
        "deviceSn": "000000",
        "paramterType": "MAX_CHARGE_CURRENT",
        "value": 0
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
