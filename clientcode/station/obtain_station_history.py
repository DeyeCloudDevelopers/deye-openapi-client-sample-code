import requests
from clientcode import variable

if __name__ == '__main__':
    url = variable.baseurl + '/station/list'
    headers = variable.headers

    """
    Retrieve history data of the station, supporting interval data queries in frames, days, months, and years.
    The meaning of granularity is as follow:
    If granularity is 1(frame), the field ‘startAt’ should be in format 'yyyy-MM-dd’. Return the data at ‘startAt’ with intervals of frame(Only support power-related data in repsonse).
    If granularity is 2(day), the field ‘startAt’ and 'endAt’should be in format 'yyyy-MM-dd’. Return the data from ‘startAt’ to ‘endAt’(excluded) (up to 31 days) with intervals of one day.
    If granularity is 3(month), the field ‘startAt’ and 'endAt’should be in format 'yyyy-MM’. Return the data for a certain number of months (up to 12 months)with intervals of one month.
    If granularity is 4(year), the field ‘startAt’ and 'endAt’should be in format 'yyyy’. Return the yearly data between ‘startAt’ to ‘endAt’.
    """
    data = {
        "stationId": 000000,        # Replace with your stationId in deyecloud
        "granularity": 1,           # The granularity of the telemetry data frame
        "startAt": "2024-05-27",    # Start date
        "endAt": "2024-08-01"       # End date
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())
