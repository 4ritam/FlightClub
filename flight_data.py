import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self._apikey = "cF2gy1ug5qkKKc3jP3h0P139e0HFGum_"

    def get_code(self, term):
        header = {
            "apikey": self._apikey
        }
        params = {
            "term": term,
            "location_types": "city"
        }
        url = "https://tequila-api.kiwi.com/locations/query"
        data = requests.get(url=url, params=params, headers=header)
        return data.json()["locations"][0]["code"]