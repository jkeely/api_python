import requests
import json
from authentication import api_key
import get_my_details
    
def main():
      url = "https://snyk.io/api/v1/org/['orgId']/integrations"
      
      payload = ""
      headers = {
        'authorization': api_key
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      values = json.loads(response.text)

      print("#################################################")
      for key, value in values.items():
            print(key,'===>'  ,value)
      print("#################################################")
      
if __name__ == "__main__":
      main()