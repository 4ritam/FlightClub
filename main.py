# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

data_object = DataManager()
flight_data_object = FlightData()
# data_object.insert_IATA_code()
data = data_object.get_data()
departing_location = "Agartala"

search_object = FlightSearch(data, departing_location)

