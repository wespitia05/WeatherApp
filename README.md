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
* Screenshot of the output for the weather app.

## Running
1) Put your **OpenWeatherMap API key** in the code (current script uses a literal string).
2) Run:
```bash
python pyqt5_weather_app.py
```

> ⚠️ **Security tip:** Avoid committing your API key to source control. See the _Use an environment variable_ section below for a safer approach.

## How it works
- When you click **Get Weather**, the app calls:
  ```text
  https://api.openweathermap.org/data/2.5/weather?q=<CITY>&appid=<API_KEY>
  ```
- The app parses the JSON response:
  - Temperature from `data["main"]["temp"]` (Kelvin) → converted to **Celsius** and **Fahrenheit** in code; the UI shows **Fahrenheit**.
  - Weather condition from `data["weather"][0]` → emoji + text description.
- Errors are caught and displayed as readable messages in the UI.

## Customize
### Units via API (optional)
Instead of converting Kelvin manually, you can request units directly:
- Imperial (°F): append `&units=imperial`
- Metric (°C): append `&units=metric`

Example:
```python
url = f\"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}\"
# Then read Fahrenheit directly from data["main"]["temp"]
```

### Use an environment variable for the API key (recommended)
Create an environment variable and read it in code to avoid hard-coding:

**macOS/Linux (bash/zsh):**
```bash
export OPENWEATHER_API_KEY="your_key_here"
```

**Windows (PowerShell):**
```powershell
setx OPENWEATHER_API_KEY "your_key_here"
# Restart your terminal to load it in new sessions
```

**Python changes:**
```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    # fall back or show a helpful message
    raise RuntimeError("Missing OPENWEATHER_API_KEY environment variable")
```

### Styling & layout
- Edit the big `setStyleSheet(""" ... """)` block for colors, fonts, and sizes.
- You can set a minimum window size or use layouts to reflow on resize.

## Troubleshooting
- **401 Unauthorized** → Invalid/missing API key.
- **404 Not Found** → City name is wrong (try `'City,CountryCode'` like `Paris,FR`).
- **Connection/Timeout** → Check your internet; VPNs/proxies/firewalls can interfere.
- **Emoji not visible** → Ensure your system font supports emoji (e.g., Segoe UI Emoji on Windows, Apple Color Emoji on macOS).

## Roadmap ideas (optional)
- Auto-detect location by IP or geolocation
- Show wind, humidity, and “feels like” temperature
- Add icons instead of emoji (e.g., PNG/SVG from a weather icon set)
- Cache last successful city and restore on launch

---

Enjoy!