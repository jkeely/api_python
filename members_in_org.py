#### NEED TO FIX #####
import requests
import json
from authentication import api_key
from get_my_details import *

def main():
      url = "https://snyk.io/api/v1/org/['orgId']/members?includeGroupAdmins="

      payload = ""
      headers = {
        'authorization': api_key
      }

      response_body = requests.request("GET", url, headers=headers, data=payload)
      values = json.loads(response_body.text)

      print(values)
      #print("#################################################")
      #print('Request Access Status: {0}'.format(values['requestAccess'][0]))
      print()
      print("#################################################")

if __name__ == "__main__":
      main()