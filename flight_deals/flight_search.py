import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv
load_dotenv()

TEQUILA_API_KEY= os.getenv("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")

class FlightSearch:
    # No hace falta poner un inicilizador cuando creo un objeto del tipo clase flightSearch, solo puedo llamar e invocar a sus funciones
    def get_destination_code(self, city_name):
        # print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        if response.status_code == 200:
            results = response.json()["locations"]
            if results:
                code = results[0]["code"]
                return code
            else:
                print("No se encontraron resultados para la búsqueda.")
        else:
            print(f"Error {response.status_code}: {response.text}")
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 14,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR",
            }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search",headers=headers,params=query)
        try:
            # me fijo en libreria como es el json 
            data = response.json()["data"][0]
            # print(f"{destination_city_code} {data['price']}")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search",headers=headers,params=query)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                deep_link= data["deep_link"],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
                )
            return flight_data
        else:
            # Creo el objeto del tipo clase FlightData y esa clase pide ciertas vbles para inizializar. 
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                deep_link= data["deep_link"]
                )
            print(f"{flight_data.destination_city}: €{flight_data.price} - Link: {flight_data.deep_link}")
            return flight_data
        
    
    