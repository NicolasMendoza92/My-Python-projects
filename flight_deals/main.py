from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_manager import UserManager
from auth_manager import AuthUser

# Creo el objeto del tipo clase UserManager para acceder a sus pros
user_info = UserManager()
# Uso de la clase AuthUser
auth_user_instance = AuthUser()

def check_flights_for_users():
    ORIGIN_CITY_IATA = "MAD"
    # Creo un objeto del tipo DataManager
    data_manager = DataManager()
    # uso el metodo get_destination
    sheet_data = data_manager.get_destination_data()
    #  creo un objeto del tipo FlightSearch para llamar a sus propiedades. 
    flight_search = FlightSearch()
    # Creo el objeto del tipo clase Notification_manager, para acceder a sus propiedades. 
    notification_manager = NotificationManager()


    # Si la primera columna de la tabla de google sheet esta vacia esta vacia, entonces: 
    if sheet_data[0]["iataCode"] == "":
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(sheet_data)

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    # seteo las fechas, la fecha de mañana para que arranque a buscar - uso timedelta de datetime
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        # le paso los parametros que defini en el metodo check_flights de la clase FlightSearch y como tiene un return de data, lo capturo en una nueva vble "flight" 
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
            )
            # Trabajo con la vble que traigo
        if flight is None:
            continue

        if flight.price < destination["lowestPrice"]:
            users = user_info.get_user_data()
            emails = [user["email"] for user in users]
            message = f" Hi!Low price alert! Only EUR{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."                     
            notification_manager.send_emails(emails, message)
            


def start():
    answer = input("Welcome to Flight Club \n Do you wanna create an user? Yes(Y)/No(N): ").upper()
    if answer == "Y":
        user_name, user_lastname, email = auth_user_instance.register()
        user_info.add_new_user(user_name, user_lastname, email)
        check_flights_for_users()      
    else:
        sure = input('We will search for flights without user... Yes(Y): ').upper()
        if sure == 'Y':
            check_flights_for_users()
        else:
            print("Good Bye!")
            

start()