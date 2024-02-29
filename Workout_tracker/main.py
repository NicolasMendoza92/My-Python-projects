import requests
from datetime import datetime
import os
from dotenv import load_dotenv


GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 180
AGE = 31

load_dotenv()

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Pido el input ejemplo: "I run 30 minutes and swim 1 hour"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# METODO POST PARA NUTRITIONNIX

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result  = response.json()
print(result)

# LO QUE HACE nutrinionnix, es analizar una frase que yo le coloque y traer los datos analizados. Entonces puedo acceder a el nombre del ejercicio

# {'exercises': [
#     {'tag_id': 317, 'user_input': 'run', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 416.26, 'photo': 
#     {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 
#     'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 
#     'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, 
#     {'tag_id': 5, 'user_input': 'cycling', 'duration_min': 20, 'met': 10, 'nf_calories': 273.33, 'photo': 
#     {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_highres.jpg', 
#     'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/5_thumb.jpg', 'is_user_uploaded': False},
#     'compendium_code': 1040, 'name': 'road cycling', 'description': None, 'benefits': None}
#     ]
#     }


sheety_endpoint = "https://api.sheety.co/d2f80af3a040d27d61c1940c780013e8/workoutTraking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            # Son los atributos que llamo aca.
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }



# METODO POST PARA SHEETY , envio los parametros con Basic Authentication
sheet_response = requests.post(sheety_endpoint, json=sheety_inputs, auth=(os.getenv("USER_SHEETY"), os.getenv("PASS_SHEETY")))

print(sheet_response.text)

#  esto me devuelve un JSON con su ID
# {
#   "workout": {
#     "date": "22/02/2024",
#     "time": "17:30:09",
#     "exercise": "Swimming",
#     "duration": 60,
#     "calories": 492,
#     "id": 3
#    }
# }