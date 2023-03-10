import requests
import os


sheety_endpoint = "https://api.sheety.co/4d0df6a0a7767a5703a77be853115f46/flightDeals/"
sheety_headers = {
    "Authorization": "Bearer nbEE9820[]9jheN",
}


class DataManager:

    def __init__(self):
        self.endpoint = f"{sheety_endpoint}/prices"
        self.response = requests.get(url=self.endpoint, headers=sheety_headers)
        self.df = self.response.json()['prices']

    def put_req(self, load_param):
        self.endpoint = f"{sheety_endpoint}/{load_param['price']['id']}"
        self.response = requests.put(url=self.endpoint, json=load_param, headers=sheety_headers)

    def get_emails(self):
        self.endpoint = f"{sheety_endpoint}/users"
        self.response = requests.get(url=self.endpoint, headers=sheety_headers)
        self.df = self.response.json()['users']
        email_list = []
        for i in self.df:
            email_list.append(i['email'])
        return email_list

