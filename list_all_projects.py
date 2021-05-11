############################################################
#
#
############################################################
import requests
import json
from authentication import api_key
import get_my_details
    
def main():
      url = "https://snyk.io/api/v1/org/['orgId']/projects"
      
      payload = ""
      headers = {
        'authorization': api_key
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      values = json.loads(response.text)
      #print(values)
      print("#################################################")
      print()
      tests = values['projects'][0]
      print(values.['id'])
      for i in values['projects']:
            print('name')
            for x in i:
                  print()

 
      print("#################################################")
      
if __name__ == "__main__":
      main()