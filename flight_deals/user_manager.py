import requests
import os
from dotenv import load_dotenv
load_dotenv()

USER_SHEETY_FLIGHT= os.getenv("USER_SHEETY_FLIGHT")
PASS_SHEETY_FLIGHT= os.getenv("PASS_SHEETY_FLIGHT")

SHEETY_PRICES_ENDPOINT_USER = "https://api.sheety.co/d2f80af3a040d27d61c1940c780013e8/flightDeals/users"

class UserManager:
    # Cuando se inicie la clase de tipo DataManager abrira un objeto vacio el cual lo ire llenando con api requests
    def __init__(self):
        self.user_data = {}
    
    def get_user_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT_USER,  auth=(USER_SHEETY_FLIGHT,PASS_SHEETY_FLIGHT))
        data = response.json()
        self.user_data = data['users']
        return self.user_data


    def add_new_user(self, user_name, user_lastname, email):
            new_user_data = {
                "user": {
                      "firstName": user_name,
                      "lastName": user_lastname,
                      "email": email,
                      }
                      }
            # debo pasarle el ID que trae en el objeto para editarlo, como parametro igual que peticion put en JS
            response = requests.post(
                url=f"{SHEETY_PRICES_ENDPOINT_USER}",
                json=new_user_data,
                auth=(USER_SHEETY_FLIGHT,PASS_SHEETY_FLIGHT)
            )
            response.raise_for_status()
            print(response.text)