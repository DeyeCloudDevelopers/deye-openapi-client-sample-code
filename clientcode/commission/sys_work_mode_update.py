import requests
from clientcode import variable

# set system work mode as SELLING_FIRST,ZERO_EXPORT_TO_LOAD or ZERO_EXPORT_TO_CT
if __name__ == '__main__':
    url = variable.baseurl + '/order/sys/workMode/update'
    headers = variable.headers
    data = {
        "deviceSn": "333333",
        "workMode": "SELLING_FIRST"     # options: SELLING_FIRST; ZERO_EXPORT_TO_LOAD; ZERO_EXPORT_TO_CT
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
