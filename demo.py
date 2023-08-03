import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data for {city_name}")
        return None


def get_temperature_for_date(weather_data, date):
    for data in weather_data['list']:
        if date in data['dt_txt']:
            return data['main']['temp']
    return None


def get_wind_speed_for_date(weather_data, date):
    for data in weather_data['list']:
        if date in data['dt_txt']:
            return data['wind']['speed']
    return None


def get_pressure_for_date(weather_data, date):
    for data in weather_data['list']:
        if date in data['dt_txt']:
            return data['main']['pressure']
    return None


def main():
    city_name = input("Enter the city name (e.g., London): ")
    weather_data = get_weather_data(city_name)

    if not weather_data:
        return

    while True:
        print("\nChoose an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temperature_for_date(weather_data, date)
            if temperature:
                print(f"Temperature on {date}: {temperature} °C")
            else:
                print("Data not available for the input date.")
        elif option == '2':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available for the input date.")
        elif option == '3':
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_for_date(weather_data, date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the input date.")
        elif option == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
