import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/station/listWithDevice'
    headers = variable.headers

    """
    Fetch station list with devices 
    DeviceType query supports: INVERTER; MICRO_INVERTER; COLLECTOR; BATTERY; MECD; METER; RELAY_BOX; OPTIMIZER; PV_MODULE.
    """
    data = {
        "page": 1,
        "size": 10,
        "deviceType": "INVERTER"
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())