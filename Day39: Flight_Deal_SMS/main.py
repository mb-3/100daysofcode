from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import datetime as dt


tomorrow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%m/%d/%Y")
end_date = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%m/%d/%Y")
ORIGIN_CITY_IATA = "LON"

notification_manager = NotificationManager()
flight_search = FlightSearch()
dm = DataManager()
sheet_data = dm.df

for i in sheet_data:
    city = i['city']
    iata_code = i['iataCode']
    if iata_code == "":
        iata_code = flight_search.get_dest_code(city)
    load_param = {'price': i}
    dm.put_req(load_param)

for destination in sheet_data:
    flight = flight_search.flight_search(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        date_from=tomorrow,
        date_to=end_date
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
