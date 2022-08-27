import requests
from flight_data import FlightData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_api = "https://api.sheety.co/16276d59486a8c0fd7fc97afa9e6760a/flightDeals/prices"
        self.data = requests.get(self.sheety_api).json()["prices"]

    def get_data(self):
        self.data = requests.get(self.sheety_api).json()["prices"]
        return self.data

    def insert_IATA_code(self):
        f_data = FlightData()
        for datasets in self.data:
            if datasets["iataCode"] == "":
                code = f_data.get_code(datasets["city"])
                body = {
                    "price": {
                        "city": datasets["city"],
                        "iataCode": code,
                        "lowestPrice": datasets["lowestPrice"]
                    }
                }
                requests.put(url=f"{self.sheety_api}/{datasets['id']}", json=body)
