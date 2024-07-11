import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/device/history'
    headers = variable.headers

    """
    Returns history data for devices at different granularities.
    granularity=1: the field ‘startAt’ should be in format 'yyyy-MM-dd’. Field ‘measurePoints’ has to be passed. Returns measure-point data for the day specified by ‘startAt’
    granularity=2: the field ‘startAt’ and 'endAt’ should be in format 'yyyy-MM-dd’. Returns statistics data between ‘startAt’ and ‘endAt’ (up to 31 days) with intervals of one day
    granularity=3: the field ‘startAt’ and 'endAt’ should be in format 'yyyy-MM’. Returns statistics data between ‘startAt’ and ‘endAt’ (up to 12 months) with intervals of one month
    granularity=4: the field ‘startAt’ and 'endAt’ should be in format 'yyyy’. Returns yearly statistics data between ‘startAt’ and ‘endAt’
    Value for field of ‘measurePoints‘ could be got through endpint ‘/v1.0/device/measurePoints’
    """
    data = {
        "deviceSn": "333333",
        "granularity": 1,
        "startAt": "2024-05-20",
        "endAt": "2024-05",
        "measurePoints": ["SOC"]
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
