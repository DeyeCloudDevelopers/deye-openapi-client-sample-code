import requests
from clientcode import variable

# Set time of use for the device
if __name__ == '__main__':
    url = variable.baseurl + '/order/sys/tou/update'
    headers = variable.headers

    # request body
    data = {
        "deviceSn": "000000",
        "timeUseSettingItems": [
            {
                "enableGeneration": True,
                "enableGridCharge": True,
                "power": 1000,
                "soc": 20,
                "time": "02:10"
            },
            {
                "enableGeneration": True,
                "enableGridCharge": False,
                "power": 2000,
                "soc": 20,
                "time": "03:15"
            },
            {
                "enableGeneration": False,
                "enableGridCharge": True,
                "power": 3000,
                "soc": 40,
                "time": "04:20"
            },
            {
                "enableGeneration": True,
                "enableGridCharge": True,
                "power": 4000,
                "soc": 50,
                "time": "05:25"
            },
            {
                "enableGeneration": False,
                "enableGridCharge": True,
                "power": 333,
                "soc": 60,
                "time": "14:00"
            },
            {
                "enableGeneration": True,
                "enableGridCharge": False,
                "power": 100,
                "soc": 70,
                "time": "15:10"
            }
        ],
        "timeoutSeconds": 30
    }

    # request post
    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
