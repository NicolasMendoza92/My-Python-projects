import requests
from datetime import datetime

USERNAME = "nicomendoza"
TOKEN = "irjflkscnmjjherewsol"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# Seteo los parametros para enviar con el metodo POST que van en el Body

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes",

}

# Primero creamos el usuario como indica la documentación de Pixela

# response = requests.post(url=pixela_endpoint, json=user_params);
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Info que va en el Header 
my_headers = {
    "X-USER-TOKEN": TOKEN
}

# Info que va en el body 
graph_config = {
    "id": "graph1",
    "name": "cycling graph", 
    "unit": "Km", 
    "type": "float", 
    "color": "ajisai"
}

# Metodo post para crear el grafico 

# response = requests.post(url=graph_endpoint, json=graph_config, headers=my_headers)
# print(response.text)

# Para ver el grafico entro a la ruta que dice la documentanción: https://pixe.la/v1/users/nicomendoza/graphs/{id del graph}

# POST
# Metodo para crear un pixel en el grafico

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixela_data = {
    # Le damos un formato a la date para que la tome la API
    "date": today.strftime("%Y%m%d"), 
    "quantity": "15", 
}

# response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=my_headers)
# print(response.text)

# UPDATE 
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixela_to_update = {
    "quantity": "11.5"
}

# response = requests.put(url=update_endpoint, json=pixela_to_update, headers=my_headers)
# print(response.text)

# DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=update_endpoint, headers=my_headers)
print(response.text)