# 🚇 MBTA Web App with Weather & Map Preview

## 👤 Author
- Christopher Gravagna and Mason Brown

## 🌟 Overview

This is aweb application helps users find the nearest MBTA station based on any Boston-area location or landmark. It also displays whether the station is wheelchair accessible, the current weather, and a Mapbox preview of the selected location.

Built with:
- 🐍 Python + Flask
- 🌐 Mapbox API (for geocoding + maps)
- 🚉 MBTA API (for real-time station info)
- 🌤️ OpenWeatherMap API (for local weather)

## 🛠️ Setup Instructions

1. Clone the repository and navigate into it.
2. Create a `.env` file with the keys for:
   - Mapbox
   - MBTA
   - OpenWeatherMap
3. Run `pip install flask python-dotenv`
4. Run `python app.py`
5. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 💡 Example Places
- Fenway Park
- TD Garden
- Boston Common

## 📌 To-Do
- Subway-only filter
- Forecast data

Team Members: Mason Brown, Chris G.

Project Overview
For this project, we built a simple Flask web app that helps users find the nearest MBTA station based on a place they enter. The app connects to the Mapbox API to get the latitude and longitude of a location and then uses the MBTA API to find the closest station. The user enters a place on the website, and it shows the nearest station and if it is wheelchair accessible. We also handled errors, so if no station is found, the app shows an error page. We followed all the basic requirements and focused on keeping it beginner-friendly.

Reflection
Development Process:
Overall, the project went pretty well. Setting up the APIs and getting the data worked out faster than we thought, but we struggled a bit with debugging JSON responses, especially when the data didn’t look like we expected. Using pprint helped a lot to see what the data looked like. Flask was new to both of us, so learning how routes, templates, and POST requests worked took some time. Running Flask in debug mode really helped find mistakes. One thing we would improve is testing more often as we built each piece, instead of waiting to test the full app.

Work Division:
At first, we planned to split the project by one person working on the API part and the other on Flask and HTML. But we both ended up doing a little of everything. We used GitHub to share our code, but sometimes we forgot to make branches and just pushed straight to main. Next time, we would use branches more and review each other’s code before merging. It worked out because we communicated often and helped each other with problems, like figuring out how to handle API errors or how to send form data.

Learning:
We both learned a lot about working with APIs and Flask. Neither of us had done this before, so figuring out how to get data from APIs and display it on a website was a good challenge. Using ChatGPT helped a ton, especially when we got stuck on small things like how to get latitude and longitude or how to handle errors in Flask. We included some screenshots below showing when we got the API working, the app running in Flask, and the error page when no station is found. One thing we wish we knew earlier was how important it is to print out the API URLs and test them in a browser—that saved us a lot of time once we started doing that.

