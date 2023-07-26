import requests

city = input("Enter the name of the city: ")

weather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={"2e388090e46bc4f3342a4bd520b6b6b1"}')

temp_kelvin=weather.json()['main']['temp']

temp_celsius = temp_kelvin - 273.15

print(f"{temp_celsius:.2f}°C")

