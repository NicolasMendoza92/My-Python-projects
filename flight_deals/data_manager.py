import requests
import os
from dotenv import load_dotenv
load_dotenv()

USER_SHEETY_FLIGHT= os.getenv("USER_SHEETY_FLIGHT")
PASS_SHEETY_FLIGHT= os.getenv("PASS_SHEETY_FLIGHT")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d2f80af3a040d27d61c1940c780013e8/flightDeals/prices"


# cities = [price["city"] for price in data["prices"]]
# iata_codes = [price["iataCode"] for price in data["prices"]]
# lowest_prices = [price["lowestPrice"] for price in data["prices"]]
# ids = [price["id"] for price in data["prices"]]

# DATA QUE ME TRAE EL GET DE SHEETY
# {
#   "prices": [
#     {
#       "city": "Roma",
#       "iataCode": "RMA",
#       "lowestPrice": 100,
#       "id": 2
#     },
#     {
#       "city": "Edinburgh",
#       "iataCode": "EDI",
#       "lowestPrice": 120,
#       "id": 3
#     },
#     {
#       "city": "Tokyo",
#       "iataCode": "TYO",
#       "lowestPrice": 550,
#       "id": 4
#     },
#   ]
# }


class DataManager:
    # Cuando se inicie la clase de tipo DataManager abrira un objeto vacio el cual lo ire llenando con api requests
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,  auth=(USER_SHEETY_FLIGHT,PASS_SHEETY_FLIGHT))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # debo pasarle el ID que trae en el objeto para editarlo, como parametro igual que peticion put en JS
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=(USER_SHEETY_FLIGHT,PASS_SHEETY_FLIGHT)
            )
            print(response.text)

