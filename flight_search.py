import datetime

import requests
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data, departing_location):
        self.data = data
        flight = FlightData()
        self._url = "https://tequila-api.kiwi.com/v2/search"
        self.departure_location_code = flight.get_code(departing_location)
        self.data_retrieve()

    def date_string(self, date):
        date_array = str(date).split(" ")[0].split('-')
        date_array.reverse()
        str1 = date_array[0]
        for i in range(1, len(date_array)):
            str1 += "/" + date_array[i]
        return str1

    def data_retrieve(self):
        header = {
            "apikey": "cF2gy1ug5qkKKc3jP3h0P139e0HFGum_"
        }
        starting_date = self.date_string(datetime.datetime.now() + datetime.timedelta(days=1))
        ending_date = self.date_string(datetime.datetime.now() + datetime.timedelta(days=60))

        data_dict = {}
        for dataset in self.data:
            body = {
                "fly_from": self.departure_location_code,
                "fly_to": dataset["iataCode"],
                "date_from": starting_date,
                "date_to": ending_date,
                "flight_type": "oneway",
                "price_to": dataset["lowestPrice"]
            }
            data = requests.get(url=self._url, headers=header, params=body).json()["data"]
            if len(data) == 0:
                break

            lowest_price = data[0]["price"]
            depart_time = str(data[0]["local_departure"]).split(".")[0].replace("-", "/").replace("T", " ")
            for i in range(1, len(data)):
                if data[1]["price"] < lowest_price:
                    lowest_price = data[1]["price"]
                    depart_time = str(data[1]["local_departure"]).split(".")[0].replace("-", "/").replace("T", " ")

            data = {
                dataset["city"]: {
                    "price": lowest_price,
                    "departure": depart_time
                }
            }
            data_dict.update(data)

        print(data_dict)
