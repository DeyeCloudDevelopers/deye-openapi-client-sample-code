import requests
from clientcode import variable

# Get the status of command execution
if __name__ == '__main__':
    orderId = '000000'   # Replace with orderId you sent
    url = variable.baseurl + '/order/' + orderId
    headers = variable.headers

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.json())
