import requests
import os
from flight_data import FlightData

teq_endpoint = os.environ['TEQ_ENDPPOINT']
headers = os.environ['TEQ_HEADERS']


class FlightSearch:

    def get_dest_code(self, location: str):
        params = {
            "term": location,
            "location_types": "airport",
        }
        response = requests.get(url=teq_endpoint, params=params, headers=headers)
        df = response.json()['locations']
        iata_code = df[0]['id']
        return iata_code

    def flight_search(self, departure_code, dest_code, date_from, date_to):

        flight_params = {
            "fly_from": departure_code,
            "fly_to": dest_code,
            "date_from": date_from,
            "date_to": date_to,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }
        response = requests.get(url=teq_endpoint, params=flight_params, headers=headers)
        print(response.json()['data'])
        try:
            df = response.json()["data"]
        except IndexError:
            print(f"No flights found for {dest_code}.")
            return None

        flight_data = FlightData(
            price=df["price"],
            origin_city=df["route"][0]["cityFrom"],
            origin_airport=df["route"][0]["flyFrom"],
            destination_city=df["route"][0]["cityTo"],
            destination_airport=df["route"][0]["flyTo"],
            out_date=df["route"][0]["local_departure"].split("T")[0],
            return_date=df["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
