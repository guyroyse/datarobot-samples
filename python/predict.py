import os
import json
import requests

from pandas import DataFrame

api_token = os.environ['DATAROBOT_API_TOKEN']
username = os.environ['DATAROBOT_API_USERNAME']
datarobot_key = os.environ['DATAROBOT_API_KEY']
deployment_id = '5c51af53969ce00199d2c9dc'

url = f"https://datarobot-predictions.orm.datarobot.com/predApi/v1.0/deployments/{deployment_id}/predictions"
auth = (username, api_token)

headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'datarobot-key': datarobot_key
}

data = DataFrame([
  {
    "horsepower": 130,
    "weight": 3504,
    "displacement": 307,
    "cylinders": 8,
    "model year": 70,
    "origin": 1,
    "acceleration": 12
  },{
    "horsepower": 165,
    "weight": 3693,
    "displacement": 350,
    "cylinders": 8,
    "model year": 70,
    "origin": 1,
    "acceleration": 11.5
  }
])

data_json = data.to_json(orient='records')

print("DataRobot Request")
print(json.dumps(json.loads(data_json), indent=2))
print()

response = requests.post(url, auth=auth, headers=headers, data=data_json)
response_json = response.json()

print("DataRobot Response")
print(json.dumps(response_json, indent=2))
print()
