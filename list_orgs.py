import requests
import json
from authentication import api_key
import get_my_details
    
def main():
      url = "https://snyk.io/api/v1/orgs"

      payload = ""
      headers = {
        'authorization': api_key
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      values = json.loads(response.text)

      print("#################################################")
      group_name = values['orgs'][0]['group']['name']
      print('Group name: {0}'.format(group_name))
      group_id = values['orgs'][0]['group']['id']
      print('Group id: {0}'.format(group_id))

      print()
      demo_name = values['orgs'][0]['name']
      print('Organization name: {0}'.format(demo_name))
      org_id = values['orgs'][0]['id']
      print('Organization id: {0}'.format(org_id))
      slug = values['orgs'][0]['slug']
      print('Slug name: {0}'.format(slug))
      url = values['orgs'][0]['url']
      print('URL: {0}'.format(url))
      print("#################################################")
      
if __name__ == "__main__":
      main()