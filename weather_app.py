import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "fr"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extraction des données importantes
        city_name = data.get("name", "Inconnue")
        temp = data["main"].get("temp", "N/A")
        humidity = data["main"].get("humidity", "N/A")
        weather_desc = data["weather"][0].get("description", "N/A")

        # Affichage des résultats
        print(f"\nMétéo à {city_name} :")
        print(f"- Température : {temp}°C")
        print(f"- Humidité : {humidity}%")
        print(f"- Description : {weather_desc.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur HTTP : {http_err}")
    except Exception as err:
        print(f"Erreur : {err}")

if __name__ == "__main__":
    print("Bienvenue dans l'application météo !")
    api_key = "738a1a808e8f517442b4e00df52c8095"  # Remplace par ta clé API OpenWeatherMap

    while True:
        city = input("\nEntrez le nom d'une ville (ou 'exit' pour quitter) : ").strip()
        if city.lower() == "exit":
            print("Au revoir !")
            break
        
        get_weather(city, api_key)
