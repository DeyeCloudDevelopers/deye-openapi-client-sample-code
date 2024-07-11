import requests
from clientcode import variable

# Set battery type
if __name__ == '__main__':
    url = variable.baseurl + '/order/battery/type/update'
    headers = variable.headers

    """
    If the inverter type is Three phase LV Hybrid or Single phase LV Hybrid, 4 battery types supported: BATT_V;
    BATT_SOC; LI; NO_BATTERY.
    
    If the inverter type is Three phase HV Hybrid, 3 battery types supported: BATT_V; LI; NO_BATTERY.
    """
    data = {
        "deviceSn": "000000",
        "batteryType": "LI"
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
