import unittest
import requests
import json

class TestApi(unittest.TestCase):
  def test_create(self):
    url = 'http://127.0.0.1:5000/users/create'
    payload = {
      "name": "John Doe",
      "age": 32,
      "adress": "5th Avenue"
    }

    headers = {
      "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    data = response.json()[0]

    self.assertEqual(data['name'], payload['name'])
    self.assertEqual(data['age'], payload['age'])
    self.assertEqual(data['adress'], payload['adress'])

  def test_update(self):
    url_create = 'http://127.0.0.1:5000/users/create'
    payload = {
      "name": "John Doe",
      "age": 32,
      "adress": "5th Avenue"
    }

    headers = {
      "Content-Type": "application/json"
    }

    response = requests.request("POST", url_create, headers=headers, data=json.dumps(payload))
    data = response.json()[0]

    id = data['id']
    url_create = f'http://127.0.0.1:5000/users/update/{id}'
    payload = {
      "name": "John Doe Ramone",
      "age": 42,
      "adress": "5th Avenue"
    }
    response = requests.request("PUT", url_create, headers=headers, data=json.dumps(payload))
    data=response.json()
    print(data)

    