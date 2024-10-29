# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan
# tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

api_key = "3a7c3b95e29fa41806ca364deb0f62cb"

paikkakunta = input("Give a place for forecast: ")

geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=1&appid={api_key}"
geo_vastaus = requests.get(geo_url).json()

if geo_vastaus:
    lat = geo_vastaus[0]["lat"]
    lon = geo_vastaus[0]["lon"]

    sää_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    sää_vastaus = requests.get(sää_url).json()

    if 'current' in sää_vastaus:
        lämpötila = sää_vastaus['current']['temp']
        säätila = sää_vastaus['current']['weather'][0]['description']
        print(f"Temperature: {lämpötila - 273.15:.1f} °C, Weather: {säätila}")
    else:
        print("Request couldn't find weather information.")
else:
    print("Couldn't find a place for forecast.")
