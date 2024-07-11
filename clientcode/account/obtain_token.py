import requests
import hashlib
from clientcode import variable
"""
The token serves as the credential for accessing resources. Currently, registration via mobile number, email address, 
or username is supported on DeyeCloud. Users can choose one of three options for login (either the mobile, email, 
or username field is required;When the field mobile is used, the field countryCode must also be included). 
If companyId is not provided, the token retrieved will correspond to the Personal user. 
When companyId is provided, the token retrieved will correspond to the business member companyId can be 
obtained through endpoints ‘/v1.0/account/info’
"""
if __name__ == '__main__':
    appId = '000000000000000'      # Replace with  your appId
    url = variable.baseurl + '/account/token?appId=' + appId
    headers = {
        'Content-Type': 'application/json'
    }
    password = '123456'             # Replace with your password for www.deyecloud.com
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    passwordWith256 = sha256_hash.hexdigest()
    data = {
            "appSecret": "000000000000000",      # Replace with your appSecret
            "email": "*****@deye.com.cn",      # Replace with your email
            "companyId": "0",                  # Replace with your companyId
            "password": passwordWith256
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()

        print(response.status_code)
        print(response.json())

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


