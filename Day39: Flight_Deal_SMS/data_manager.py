import requests
import os

sheety_auth = os.environ['SHEETY_AUTH']
sheety_endpoint = os.environ['SHEETY_ENDPOINT']
sheety_headers = os.environ['SHEETY_HEADERS']


class DataManager:

    def __init__(self):
        self.endpoint = sheety_endpoint
        self.response = requests.get(url=self.endpoint, headers=sheety_headers)
        self.df = self.response.json()['prices']

    def put_req(self, load_param):
        self.endpoint = f"{sheety_endpoint}/{load_param['price']['id']}"
        self.response = requests.put(url=self.endpoint, json=load_param, headers=sheety_headers)

