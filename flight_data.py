import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    sheety_api = "https://api.sheety.co/16276d59486a8c0fd7fc97afa9e6760a/flightDeals/prices"
    price_list = requests.get(sheety_api).json()["prices"]
    print(price_list)
