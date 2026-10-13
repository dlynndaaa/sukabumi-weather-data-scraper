import pandas as pd
import time
import io
import urllib.request
from urllib.error import HTTPError

# 1. Daftar lengkap 47 Kecamatan di Kab. Sukabumi (koordinat disesuaikan dengan file acuan dosen & perbaikan Cidolog)
kecamatan_data = [
    {"kode": "32.02.01", "nama": "Cibadak", "lat": -6.9356, "lon": 106.7892},
    {"kode": "32.02.02", "nama": "Nagrak", "lat": -6.8417, "lon": 106.8189},
    {"kode": "32.02.03", "nama": "Cicurug", "lat": -6.7814, "lon": 106.7825},
    {"kode": "32.02.04", "nama": "Cidadap", "lat": -6.6989, "lon": 106.7936},
    {"kode": "32.02.05", "nama": "Cikidang", "lat": -6.8236, "lon": 106.7019},
    {"kode": "32.02.06", "nama": "Warungkiara", "lat": -6.8958, "lon": 106.6750},
    {"kode": "32.02.07", "nama": "Kalibunder", "lat": -7.1833, "lon": 106.6333},
    {"kode": "32.02.08", "nama": "Surade", "lat": -7.3417, "lon": 106.5667},
    {"kode": "32.02.09", "nama": "Ciemas", "lat": -7.2333, "lon": 106.5167},
    {"kode": "32.02.10", "nama": "Waluran", "lat": -7.1667, "lon": 106.5833},
    {"kode": "32.02.11", "nama": "Jampangkulon", "lat": -7.2833, "lon": 106.4667},
    {"kode": "32.02.12", "nama": "Cimanggu", "lat": -7.3667, "lon": 106.5167},
    {"kode": "32.02.13", "nama": "Kalapa Nunggal", "lat": -6.9667, "lon": 106.9167},
    {"kode": "32.02.14", "nama": "Cisaat", "lat": -6.8833, "lon": 106.9333},
    {"kode": "32.02.15", "nama": "Gunungguruh", "lat": -6.9167, "lon": 106.8667},
    {"kode": "32.02.16", "nama": "Kabandungan", "lat": -6.7667, "lon": 106.6833},
    {"kode": "32.02.17", "nama": "Kadudampit", "lat": -6.8333, "lon": 106.7500},
    {"kode": "32.02.18", "nama": "Cibitung", "lat": -6.9500, "lon": 106.5167},
    {"kode": "32.02.19", "nama": "Cikakak", "lat": -7.0167, "lon": 106.5667},
    {"kode": "32.02.20", "nama": "Parungkuda", "lat": -6.9000, "lon": 106.7667},
    {"kode": "32.02.21", "nama": "Sukabumi", "lat": -6.9167, "lon": 106.9333},
    {"kode": "32.02.22", "nama": "Sukaraja", "lat": -6.8667, "lon": 106.9500},
    {"kode": "32.02.23", "nama": "Parakansalak", "lat": -6.7167, "lon": 106.7333},
    {"kode": "32.02.24", "nama": "Cicantayan", "lat": -6.8000, "lon": 106.8333},
    {"kode": "32.02.25", "nama": "Cidahu", "lat": -6.7333, "lon": 106.8500},
    {"kode": "32.02.26", "nama": "Cikembar", "lat": -6.8167, "lon": 106.8167},
    {"kode": "32.02.27", "nama": "Ciambar", "lat": -6.7500, "lon": 106.8000},
    {"kode": "32.02.28", "nama": "Gegerbitung", "lat": -6.8833, "lon": 106.8167},
    {"kode": "32.02.29", "nama": "Sagaranten", "lat": -6.7833, "lon": 106.7167},
    {"kode": "32.02.30", "nama": "Curugkembar", "lat": -6.7333, "lon": 106.6833},
    {"kode": "32.02.31", "nama": "Purabaya", "lat": -6.9667, "lon": 106.5667},
    {"kode": "32.02.32", "nama": "Nyalindung", "lat": -7.0667, "lon": 106.9333},
    {"kode": "32.02.33", "nama": "Cireunghas", "lat": -7.1167, "lon": 106.8667},
    {"kode": "32.02.34", "nama": "Sukalarang", "lat": -7.1667, "lon": 106.8667},
    {"kode": "32.02.35", "nama": "Sukanagara", "lat": -7.0833, "lon": 107.0167},
    {"kode": "32.02.36", "nama": "Tegalbuleud", "lat": -7.4167, "lon": 106.6333},
    {"kode": "32.02.37", "nama": "Cidolog", "lat": -7.3170, "lon": 106.8390},
    {"kode": "32.02.38", "nama": "Caringin", "lat": -6.7167, "lon": 106.8167},
    {"kode": "32.02.39", "nama": "Bojonggenteng", "lat": -7.2667, "lon": 106.6833},
    {"kode": "32.02.40", "nama": "Bantargadung", "lat": -7.1333, "lon": 106.7333},
    {"kode": "32.02.41", "nama": "Cibitung", "lat": -6.9500, "lon": 106.5167},
    {"kode": "32.02.42", "nama": "Cisolok", "lat": -6.9833, "lon": 106.4167},
    {"kode": "32.02.43", "nama": "Cikidang", "lat": -6.8236, "lon": 106.7019},
    {"kode": "32.02.44", "nama": "Lengkong", "lat": -6.8667, "lon": 106.7167},
    {"kode": "32.02.45", "nama": "Jampangtengah", "lat": -7.0833, "lon": 106.8000},
    {"kode": "32.02.46", "nama": "Warungkiara", "lat": -6.8958, "lon": 106.6750},
    {"kode": "32.02.47", "nama": "Cireunghas", "lat": -7.1167, "lon": 106.8667}
]

# 2. Daftar tahun yang akan diunduh
daftar_tahun = [2020, 2021, 2022, 2023, 2024, 2025]

# 3. Proses unduh per tahun
for tahun in daftar_tahun:
    print(f"\n==========================================")
    print(f"  Memulai download data tahun {tahun}")
    print(f"==========================================")
    data_tahunan = []
    
    start_date = f"{tahun}-01-01"
    end_date = f"{tahun}-12-31"
    
    for i, kec in enumerate(kecamatan_data, start=1):
        kode = kec["kode"]
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
        
        sukses = False
        percobaan = 0
        
        while not sukses and percobaan < 4:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=20) as response:
                    content = response.read().decode('utf-8')
                
                # Pastikan respons memuat data CSV cuaca yang valid
                if "temperature_2m_mean" in content:
                    df_kec = pd.read_csv(io.StringIO(content), skiprows=3)
                    
                    df_kec.insert(0, "kabupaten", "Sukabumi")
                    df_kec.insert(1, "kode_kecamatan", kode)
                    df_kec.insert(2, "nama_kecamatan", nama)
                    df_kec.insert(3, "latitude", lat)
                    df_kec.insert(4, "longitude", lon)
                    
                    data_tahunan.append(df_kec)
                    print(f"[{tahun}] ({i}/47) Berhasil: [{kode}] {nama}")
                    sukses = True
                    time.sleep(1.0)
                else:
                    percobaan += 1
                    print(f"[{tahun}] ({i}/47) Respons tidak valid untuk {nama}. Coba ulang ({percobaan}/4)...")
                    time.sleep(3)
                    
            except HTTPError as e:
                percobaan += 1
                if e.code == 429:
                    print(f"[{tahun}] ({i}/47) Rate limit untuk {nama}. Menunggu jeda 12 detik ({percobaan}/4)...")
                    time.sleep(12)
                else:
                    print(f"[{tahun}] ({i}/47) HTTP Error {e.code} pada {nama}. Coba ulang ({percobaan}/4)...")
                    time.sleep(3)
            except Exception as e:
                percobaan += 1
                print(f"[{tahun}] ({i}/47) Kendala jaringan pada {nama}: {e}. Coba ulang ({percobaan}/4)...")
                time.sleep(3)
                
        if not sukses:
            print(f"--> PERINGATAN: Gagal mengunduh {nama} setelah 4 kali percobaan.")

    # Simpan hasil gabungan per tahun ke format CSV
    if data_tahunan:
        df_final_tahun = pd.concat(data_tahunan, ignore_index=True)
        nama_file = f"cuaca_kab_sukabumi_{tahun}.csv"
        df_final_tahun.to_csv(nama_file, index=False)
        print(f"==> Berkas {nama_file} berhasil disimpan ({len(df_final_tahun)} baris).")

# 4. Pengunduhan otomatis ke perangkat lokal (khusus Google Colab)
try:
    from google.colab import files
    for tahun in daftar_tahun:
        files.download(f"cuaca_kab_sukabumi_{tahun}.csv")
except ImportError:
    pass
