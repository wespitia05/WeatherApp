# PyQt5 Weather App

A minimal desktop **Weather App** built with **PyQt5** and the **OpenWeatherMap** API. Enter a city name, click **Get Weather**, and the app shows the current **temperature (°F)**, a weather **emoji**, and a brief **description**. Includes friendly error messages for common HTTP issues.

## Features
- 🔎 Search by **city name**
- 🌡️ Displays temperature (converted to **Fahrenheit**), plus a matching **emoji**
- 📝 Shows a short **weather description** (e.g., `light rain`)
- 🧯 Robust error handling with readable messages (400/401/403/404/5xx, connection, timeout, etc.)
- 🧩 Single-file script: `pyqt5_weather_app.py`

## Requirements
- Python 3.8+
- PyQt5
- requests
- An **OpenWeatherMap API key** (free tier available)

Install locally:
```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate       # Windows PowerShell

pip install PyQt5 requests
```

## Project structure
```
.
└── pyqt5_weather_app.py
```

## Screenshots
![Weather App Screenshot](weather_app_ss.png)
* Screenshot of the output for the digital clock.
