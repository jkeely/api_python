####
import requests
import json
from authentication import api_key

def main():
      url ="https://snyk.io/api/v1/user/me"
      
      payload = ""
      headers = {
        'authorization': api_key
      }

      response_body = requests.request("GET", url, headers=headers, data=payload)
      values = json.loads(response_body.text)
      
      print("#################################################")
      print('User Id: {0}'.format(values['id']))
      print('Username: {0}'.format(values['username']))
      print('Email: {0}'.format(values['email']))
      print()
      group_name = values['orgs'][0]['group']['name']
      print('Group name: {0}'.format(group_name))
      group_id = values['orgs'][0]['group']['id']
      print('Group id: {0}'.format(group_id))
      print()
      demo_name = values['orgs'][0]['name']
      print('Organization name: {0}'.format(demo_name))
      orgId = values['orgs'][0]['id']
      print('Organization id: {0}'.format(orgId))
      print("#################################################")
      
if __name__ == "__main__":
      main()