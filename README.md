# ⛅ Sukabumi Weather Data Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![API](https://img.shields.io/badge/API-Open_Meteo-0078D4?style=for-the-badge)

An automated Python script to extract daily historical weather data for all 47 sub-districts in Sukabumi Regency from 2020 to 2025 using the Open-Meteo Historical Weather API.

## Coverage & Parameters
- Region: 47 Sub-districts in Sukabumi Regency, West Java, Indonesia.
- Time Range: January 1, 2020 – December 31, 2025.
- Weather Variables:
  * `temperature_2m_mean`: Daily mean temperature (°C)
  * `precipitation_sum`: Daily precipitation total (mm)
  * `relative_humidity_2m_mean`: Daily mean relative humidity (%)
  * `wind_speed_10m_max`: Maximum wind speed at 10 meters (km/h)

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/dlynndaaa/sukabumi-weather-data-scraper.git
   cd sukabumi-weather-data-scraper
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the scraper:
   ```bash
   python src/scraper.py
 The annual CSV files will be saved automatically in the data/ directory.
