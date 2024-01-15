import schedule
import time

def weather(latitude,longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data

def weather_update():
    #latitude and longitude for Toronto, Canada 
    latitude = 43.6532
    longitude = -79.3470

    weather_data = weather(latitude,longitude)
    temperature = weather_data["hourly"]["temperature_2m"]
    relativehumdity = weather_data["hourly"]["relativehumidty_2m"]
    windspeed = weather_data["hourly"]["windspeed_10m"]



def main():
    schedule.every().day.at("8:00").do(weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
