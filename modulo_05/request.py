import requests
import json

url = 'https://as5jmctylk.execute-api.us-east-1.amazonaws.com/default/demo_forecast'

data = {
  "Sem Experiencia": 0,
  "Com Experiencia": 1
}

print(type(data))

request = requests.post(
  url,
  data=json.dumps(data),
  verify=False
)

response = request.json()
print('==========================')
print('===       RESPONSE     ===')
print('==========================')
print('Response:', response)
print('Type', type(response))
print(response['Com Experiencia'] - response['Sem Experiencia'])