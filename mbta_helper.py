import os
import json
import urllib.request
from urllib.parse import quote
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

def get_json(url):
    """Fetch and return the JSON response from a URL."""
    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)

def get_lat_lng(place_name):
    """Get the latitude and longitude of a place using Mapbox."""
    query = quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=address,place,poi"
    data = get_json(url)

    if not data["features"]:
        raise ValueError("Could not find location.")

    coordinates = data["features"][0]["geometry"]["coordinates"]
    return str(coordinates[1]), str(coordinates[0])  # Return (lat, lon)

def get_nearest_station(latitude, longitude):
    """Find the nearest MBTA station to given coordinates."""
    url = f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    data = get_json(url)

    if not data["data"]:
        return "No nearby stations found", False

    stop = data["data"][0]["attributes"]
    station_name = stop["name"]
    accessible = stop["wheelchair_boarding"] == 1  # 1 = accessible, 2 = not accessible
    return station_name, accessible

def find_stop_near(place_name):
    """Main function to find the nearest MBTA stop to a place name."""
    lat, lng = get_lat_lng(place_name)
    return get_nearest_station(lat, lng)

def main():
    """For quick testing in the terminal."""
    place = "Fenway Park"  # Try something like "Boston Common" or "TD Garden"
    try:
        lat, lng = get_lat_lng(place)
        print(f"Coordinates of {place}: {lat}, {lng}")
        stop, accessible = get_nearest_station(lat, lng)
        print(f"Nearest Stop: {stop}, Accessible: {'Yes' if accessible else 'No'}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
