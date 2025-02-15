# Weather App

A simple GUI-based Weather App built using **Python** and **Tkinter**, with real-time weather data fetched from the OpenWeather API.

## Features
- Search for any city's current weather.
- Displays temperature, humidity, wind speed, and weather description.
- Shows local time and date based on the city's timezone.
- User-friendly interface with a visually appealing design.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Dependencies
Make sure you have the following Python packages installed:
```sh
pip install tkinter geopy timezonefinder pytz requests pillow
```

## Usage
- Enter the city name in the search box.
- Click the search button to fetch weather data.
- The app will display temperature, humidity, wind speed, and more.

## API Key Setup
This app uses the OpenWeather API. Get an API key from [OpenWeather](https://openweathermap.org/api) and update the `API_KEY` in `main.py`:
```python
API_KEY = "your_api_key_here"
```

## Screenshots
![Weather App Screenshot](screenshot.png)

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, contact **your-email@example.com**.

