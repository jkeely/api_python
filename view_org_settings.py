####
import requests
import json
from authentication import api_key
from get_my_details import *


request_url = "https://snyk.io/api/v1/org/['orgId']/settings"

payload = ""
headers = {
  'authorization': api_key
}

response_body = requests.request("GET", request_url, headers=headers, data=payload)
values = json.loads(response_body.text)

print("#################################################")
print()
print('Request Access Status: {0}'.format(values['requestAccess']['enabled']))
print()
print("#################################################")