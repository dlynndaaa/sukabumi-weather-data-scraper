import os
import time
import pandas as pd

kecamatan_data = [
    {"nama": "Bantargadung", "lat": -7.000, "lon": 106.666},
    {"nama": "Bojonggenteng", "lat": -6.820, "lon": 106.710},
    {"nama": "Caringin", "lat": -6.870, "lon": 106.870},
    {"nama": "Ciambar", "lat": -6.830, "lon": 106.780},
    {"nama": "Cibadak", "lat": -6.890, "lon": 106.780},
    {"nama": "Cibitung", "lat": -7.340, "lon": 106.610},
    {"nama": "Cicantayan", "lat": -6.900, "lon": 106.840},
    {"nama": "Cicurug", "lat": -6.780, "lon": 106.770},
    {"nama": "Cidadap", "lat": -7.260, "lon": 106.880},
    {"nama": "Cidahu", "lat": -6.760, "lon": 106.740},
    {"nama": "Cidolog", "lat": -7.250, "lon": 106.820},
    {"nama": "Ciemas", "lat": -7.160, "lon": 106.510},
    {"nama": "Cikakak", "lat": -6.950, "lon": 106.500},
    {"nama": "Cikembar", "lat": -6.970, "lon": 106.800},
    {"nama": "Cikidang", "lat": -6.910, "lon": 106.680},
    {"nama": "Cimanggu", "lat": -7.220, "lon": 106.670},
    {"nama": "Ciracap", "lat": -7.300, "lon": 106.470},
    {"nama": "Cireunghas", "lat": -6.970, "lon": 107.030},
    {"nama": "Cisaat", "lat": -6.900, "lon": 106.890},
    {"nama": "Cisolok", "lat": -6.930, "lon": 106.440},
    {"nama": "Curugkembar", "lat": -7.210, "lon": 106.960},
    {"nama": "Gegerbitung", "lat": -7.030, "lon": 107.010},
    {"nama": "Gunungguruh", "lat": -6.940, "lon": 106.870},
    {"nama": "Jampang Kulon", "lat": -7.290, "lon": 106.590},
    {"nama": "Jampang Tengah", "lat": -7.060, "lon": 106.810},
    {"nama": "Kabandungan", "lat": -6.750, "lon": 106.610},
    {"nama": "Kadudampit", "lat": -6.860, "lon": 106.900},
    {"nama": "Kalapanunggal", "lat": -6.790, "lon": 106.670},
    {"nama": "Kalibunder", "lat": -7.270, "lon": 106.700},
    {"nama": "Kebonpedes", "lat": -6.950, "lon": 106.970},
    {"nama": "Lengkong", "lat": -7.110, "lon": 106.730},
    {"nama": "Nagrak", "lat": -6.870, "lon": 106.810},
    {"nama": "Nyalindung", "lat": -7.030, "lon": 106.940},
    {"nama": "Pabuaran", "lat": -7.170, "lon": 106.770},
    {"nama": "Palabuhanratu", "lat": -6.980, "lon": 106.540},
    {"nama": "Parakansalak", "lat": -6.790, "lon": 106.730},
    {"nama": "Parungkuda", "lat": -6.830, "lon": 106.750},
    {"nama": "Purabaya", "lat": -7.110, "lon": 106.880},
    {"nama": "Sagaranten", "lat": -7.180, "lon": 106.880},
    {"nama": "Simpenan", "lat": -7.050, "lon": 106.570},
    {"nama": "Sukabumi", "lat": -6.880, "lon": 106.930},
    {"nama": "Sukalarang", "lat": -6.920, "lon": 107.030},
    {"nama": "Sukaraja", "lat": -6.920, "lon": 106.960},
    {"nama": "Surade", "lat": -7.340, "lon": 106.550},
    {"nama": "Tegalbuleud", "lat": -7.410, "lon": 106.660},
    {"nama": "Waluran", "lat": -7.210, "lon": 106.550},
    {"nama": "Warungkiara", "lat": -7.030, "lon": 106.710}
]

daftar_tahun = [2020, 2021, 2022, 2023, 2024, 2025]
os.makedirs("data", exist_ok=True)

for tahun in daftar_tahun:
    print(f"\n--- Memulai download data tahun {tahun} ---")
    data_tahunan = []
    
    start_date = f"{tahun}-01-01"
    end_date = f"{tahun}-12-31"
    
    for kec in kecamatan_data:
        nama = kec["nama"]
        lat = kec["lat"]
        lon = kec["lon"]
        
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={lat}&longitude={lon}"
            f"&start_date={start_date}&end_date={end_date}"
            f"&daily=temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean,wind_speed_10m_max"
            f"&timezone=Asia%2FJakarta"
            f"&format=csv"
        )
        
        try:
            df_kec = pd.read_csv(url, skiprows=3)
            df_kec.insert(0, "kabupaten", "Sukabumi")
            df_kec.insert(1, "kecamatan", nama)
            data_tahunan.append(df_kec)
            print(f"[{tahun}] Berhasil mengambil: {nama}")
        except Exception as e:
            print(f"[{tahun}] Gagal mengambil {nama}: {e}")
            
        time.sleep(0.3)
    
    if data_tahunan:
        df_final_tahun = pd.concat(data_tahunan, ignore_index=True)
        nama_file = f"data/cuaca_kab_sukabumi_{tahun}.csv"
        df_final_tahun.to_csv(nama_file, index=False)
        print(f"==> Berkas {nama_file} tersimpan! Total baris: {len(df_final_tahun)}")
