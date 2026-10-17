# ⛅ Sukabumi Weather Data Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![API](https://img.shields.io/badge/API-Open_Meteo-0078D4?style=for-the-badge)

An automated Python script to extract daily historical weather data for all 47 sub-districts in Sukabumi Regency from 2020 to 2025 using the Open-Meteo Historical Weather API.

## 📊 Sample Data Output (CSV)
The script generates annual CSV files saved automatically in the `data/` directory. Here is a preview of the extracted data structure:
<img width="1524" height="221" alt="output-sample-weather-data" src="https://github.com/user-attachments/assets/569c139d-ff2f-4bd5-92ec-6a236f5550d5" />

## 📍 Coverage & Parameters
- **Region:** 47 Sub-districts in Sukabumi Regency, West Java, Indonesia.
- **Time Range:** January 1, 2020 – December 31, 2025.
- **Extracted Data Columns:**
  - `kabupaten` & `nama_kecamatan` : Region identifiers
  - `kode_kecamatan` : Official sub-district code
  - `latitude` & `longitude` : Geospatial coordinates
  - `time` : Date of the weather record
  - `temperature_2m_mean (°C)` : Daily mean temperature
  - `precipitation_sum (mm)` : Daily precipitation total
  - `relative_humidity_2m_mean (%)` : Daily mean relative humidity
  - `wind_speed_10m_max (km/h)` : Maximum wind speed at 10 meters

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
