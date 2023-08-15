import requests

#
# Kibana REST examples
#
# Taken from https://www.elastic.co/guide/en/kibana/current/spaces-api.html
#
# Replace the following to match your cluster.
#  
ELASTIC_USER = "elastic_user"
ELASTIC_PASSWORD = 'elastic_password'
ELASTIC_NAMESPACE = "elastic"

#
# GET
#
endpoint = "index_management/indices"
endpoint = "features"
url = "http://kibana-sample-kb-http." + ELASTIC_NAMESPACE + ".svc.cluster.local:5601/api/" + endpoint
response = requests.get(url, auth=(ELASTIC_USER, ELASTIC_PASSWORD), verify=False)
print(f'=> GET: response = {response}')
print(f'=> text = {response.json()[0]}')
print(f'=>')

#
# POST
#
endpoint = "spaces/space"
url = "http://kibana-sample-kb-http." + ELASTIC_NAMESPACE + ".svc.cluster.local:5601/api/" + endpoint
headers = {'Content-Type': 'application/json', 'kbn-xsrf': 'true'}
data = '{"id":"sales", "name": "Sales", "description": "This is your Sales Space!", "disabledFeatures": [] }'
response = requests.post(url, json=data, auth=(ELASTIC_USER, ELASTIC_PASSWORD), headers=headers, verify=False)
print(f'=> POST: response = {response}')
print(f'=> POST: text = {response.json()}')
print(f'=>')

#
# GET
#
endpoint = "spaces/space/sales"
url = "http://kibana-sample-kb-http." + ELASTIC_NAMESPACE + ".svc.cluster.local:5601/api/" + endpoint
response = requests.get(url, auth=(ELASTIC_USER, ELASTIC_PASSWORD), verify=False)
print(f'=> GET: response = {response}')
print(f'=> text = {response.text}')
print(f'=>')

#
# DELETE
#
# endpoint = "spaces/space/sales"
# url = "http://kibana-sample-kb-http." + ELASTIC_NAMESPACE + ".svc.cluster.local:5601/api/" + endpoint
response = requests.delete(url, auth=(ELASTIC_USER, ELASTIC_PASSWORD), headers=headers, verify=False)
print(f'=> DELETE: result = {response}')
print(f'=>')
