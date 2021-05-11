#### Clean up out put - Delete output from authentication and get_my_details #####
import requests
import json
from authentication import api_key
from get_my_details import *

def main():
      url = "https://snyk.io/api/v1/org/['orgId']/webhooks"

      payload = ""
      headers = {
        'authorization': api_key
      }

      response_body = requests.request("GET", url, headers=headers, data=payload)
      values = json.loads(response_body.text)

      print()
      print("#################################################")
      print('The total number of webhooks: {0}'.format(values['total']))
      print('Results: {0}'.format(values['results']))
      print()
      print("#################################################")


if __name__ == "__main__":
      main()