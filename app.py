from flask import Flask, render_template, request
from mbta_helper import find_stop_near, get_lat_lng
import os
import urllib.request, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nearest_mbta", methods=["POST"])
def nearest_mbta():
    place = request.form.get("place")
    try:
        stop_name, accessible = find_stop_near(place)
        lat, lon = get_lat_lng(place)

        weather_key = os.getenv("WEATHER_API_KEY")
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=imperial"
        with urllib.request.urlopen(weather_url) as response:
            weather_data = json.loads(response.read().decode())
        temp = weather_data["main"]["temp"]
        desc = weather_data["weather"][0]["description"]

        mapbox_token = os.getenv("MAPBOX_TOKEN")
        return render_template("mbta_station.html", place=place, stop=stop_name, accessible="Yes" if accessible else "No", lat=lat, lon=lon, temp=temp, desc=desc, mapbox_token=mapbox_token)
    except Exception as e:
        print("Error:", e)
        return render_template("mbta_station.html", place=place, stop="Not found", accessible="N/A")

if __name__ == "__main__":
    app.run(debug=True)
