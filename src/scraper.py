import pandas as pd
import time
import io
import re
import urllib.request
from urllib.error import HTTPError

kecamatan_data = [
    {"kode": "32.02.01", "nama": "Pelabuhanratu",   "lat": -6.9875, "lon": 106.5512},
    {"kode": "32.02.02", "nama": "Simpenan",        "lat": -7.0650, "lon": 106.5820},
    {"kode": "32.02.03", "nama": "Cikakak",         "lat": -6.9350, "lon": 106.5120},
    {"kode": "32.02.04", "nama": "Bantargadung",    "lat": -7.0180, "lon": 106.6650},
    {"kode": "32.02.05", "nama": "Cisolok",         "lat": -6.9120, "lon": 106.4520},
    {"kode": "32.02.06", "nama": "Cikidang",        "lat": -6.8850, "lon": 106.6550},
    {"kode": "32.02.07", "nama": "Lengkong",        "lat": -7.1333, "lon": 106.7333},
    {"kode": "32.02.08", "nama": "Jampangtengah",   "lat": -7.0833, "lon": 106.8000},
    {"kode": "32.02.09", "nama": "Warungkiara",     "lat": -6.9820, "lon": 106.7120},
    {"kode": "32.02.10", "nama": "Cikembar",        "lat": -6.9650, "lon": 106.8150},
    {"kode": "32.02.11", "nama": "Cibadak",         "lat": -6.9000, "lon": 106.7667},
    {"kode": "32.02.12", "nama": "Nagrak",          "lat": -6.8417, "lon": 106.8189},
    {"kode": "32.02.13", "nama": "Parungkuda",      "lat": -6.8450, "lon": 106.7600},
    {"kode": "32.02.14", "nama": "Bojonggenteng",   "lat": -6.8180, "lon": 106.7250},
    {"kode": "32.02.15", "nama": "Parakansalak",    "lat": -6.8050, "lon": 106.6950},
    {"kode": "32.02.16", "nama": "Cicurug",         "lat": -6.7814, "lon": 106.7825},
    {"kode": "32.02.17", "nama": "Cidahu",          "lat": -6.7750, "lon": 106.7350},
    {"kode": "32.02.18", "nama": "Kalapanunggal",   "lat": -6.7980, "lon": 106.6650},
    {"kode": "32.02.19", "nama": "Kabandungan",     "lat": -6.7920, "lon": 106.5950},
    {"kode": "32.02.20", "nama": "Waluran",         "lat": -7.2150, "lon": 106.6150},
    {"kode": "32.02.21", "nama": "Jampangkulon",    "lat": -7.2650, "lon": 106.5850},
    {"kode": "32.02.22", "nama": "Ciemas",          "lat": -7.2333, "lon": 106.5167},
    {"kode": "32.02.23", "nama": "Kalibunder",      "lat": -7.2350, "lon": 106.6850},
    {"kode": "32.02.24", "nama": "Surade",          "lat": -7.3417, "lon": 106.5667},
    {"kode": "32.02.25", "nama": "Cibitung",        "lat": -7.3650, "lon": 106.6350},
    {"kode": "32.02.26", "nama": "Ciracap",         "lat": -7.3350, "lon": 106.4650},
    {"kode": "32.02.27", "nama": "Gunungguruh",     "lat": -6.9480, "lon": 106.8750},
    {"kode": "32.02.28", "nama": "Cicantayan",      "lat": -6.9250, "lon": 106.8350},
    {"kode": "32.02.29", "nama": "Cisaat",          "lat": -6.9050, "lon": 106.8850},
    {"kode": "32.02.30", "nama": "Kadudampit",      "lat": -6.8350, "lon": 106.8850},
    {"kode": "32.02.31", "nama": "Caringin",        "lat": -6.8550, "lon": 106.8450},
    {"kode": "32.02.32", "nama": "Sukabumi",        "lat": -6.8650, "lon": 106.9250},
    {"kode": "32.02.33", "nama": "Sukaraja",        "lat": -6.8850, "lon": 106.9650},
    {"kode": "32.02.34", "nama": "Kebonpedes",      "lat": -6.9450, "lon": 106.9550},
    {"kode": "32.02.35", "nama": "Cireunghas",      "lat": -6.9350, "lon": 106.9950},
    {"kode": "32.02.36", "nama": "Sukalarang",      "lat": -6.8850, "lon": 107.0050},
    {"kode": "32.02.37", "nama": "Pabuaran",        "lat": -7.1950, "lon": 106.7650},
    {"kode": "32.02.38", "nama": "Purabaya",        "lat": -7.1167, "lon": 106.8667},
    {"kode": "32.02.39", "nama": "Nyalindung",      "lat": -7.0350, "lon": 106.9250},
    {"kode": "32.02.40", "nama": "Gegerbitung",     "lat": -6.9950, "lon": 106.9850},
    {"kode": "32.02.41", "nama": "Sagaranten",      "lat": -7.2150, "lon": 106.8850},
    {"kode": "32.02.42", "nama": "Curugkembar",     "lat": -7.2650, "lon": 106.9150},
    {"kode": "32.02.43", "nama": "Cidolog",         "lat": -7.3170, "lon": 106.8390},
    {"kode": "32.02.44", "nama": "Cidadap",         "lat": -7.3150, "lon": 106.9450},
    {"kode": "32.02.45", "nama": "Tegalbuleud",     "lat": -7.3650, "lon": 106.7350},
    {"kode": "32.02.46", "nama": "Cimanggu",        "lat": -7.2850, "lon": 106.6450},
    {"kode": "32.02.47", "nama": "Ciambar",         "lat": -6.8000, "lon": 106.8150}
]

def norm_nama(teks):
    s = re.sub(r"[^a-z0-9]", "", str(teks).lower())
    return s.replace("palabuhan", "pelabuhan")

try:
    import geopandas as gpd
    print("Mengunduh poligon resmi GADM 4.1 Level 3 untuk sinkronisasi titik tengah kecamatan...")
    url_gadm = "https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_IDN_3.json.zip"
    gdf = gpd.read_file(url_gadm)

    mask_jabar = gdf["NAME_1"].apply(lambda x: re.sub(r"[^a-z0-9]", "", str(x).lower()) == "jawabarat")
    mask_suka  = gdf["NAME_2"].str.lower().str.contains("sukabumi", na=False)
    mask_kota  = gdf["NAME_2"].str.lower().str.contains("kota|city", na=False)
    if "ENGTYPE_2" in gdf.columns:
        mask_kota = mask_kota | gdf["ENGTYPE_2"].str.lower().str.contains("city|municipality", na=False)

    kec_gadm = gdf[mask_jabar & mask_suka & (~mask_kota)].copy()
    kec_gadm = kec_gadm.to_crs(epsg=4326)

    pts = kec_gadm.geometry.representative_point()
    kec_gadm["lat_gadm"] = pts.y.round(4)
    kec_gadm["lon_gadm"] = pts.x.round(4)
    kec_gadm["key_norm"] = kec_gadm["NAME_3"].apply(norm_nama)

    lookup_gadm = kec_gadm.set_index("key_norm")[["NAME_3", "lat_gadm", "lon_gadm"]].to_dict("index")

    terupdate = 0
    for item in kecamatan_data:
        k = norm_nama(item["nama"])
        if k in lookup_gadm:
            item["nama"] = lookup_gadm[k]["NAME_3"]
            item["lat"]  = float(lookup_gadm[k]["lat_gadm"])
            item["lon"]  = float(lookup_gadm[k]["lon_gadm"])
            terupdate += 1

    print(f"--> Berhasil menyelaraskan {terupdate}/{len(kecamatan_data)} titik koordinat tepat di dalam poligon GADM!")
except Exception as e:
    print(f"--> Info: Menggunakan koordinat tabel utama ({e}).")

daftar_tahun = [2020, 2021, 2022, 2023, 2024, 2025]
semua_tahun_df = []

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

                if "temperature_2m_mean" in content:
                    df_kec = pd.read_csv(io.StringIO(content), skiprows=3)

                    df_kec.insert(0, "kabupaten", "Sukabumi")
                    df_kec.insert(1, "kode_kecamatan", kode)
                    df_kec.insert(2, "nama_kecamatan", nama)
                    df_kec.insert(3, "latitude", lat)
                    df_kec.insert(4, "longitude", lon)

                    data_tahunan.append(df_kec)
                    print(f"[{tahun}] ({i}/47) Berhasil: [{kode}] {nama} ({lat}, {lon})")
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

    if data_tahunan:
        df_final_tahun = pd.concat(data_tahunan, ignore_index=True)
        nama_file = f"cuaca_kab_sukabumi_{tahun}.csv"
        df_final_tahun.to_csv(nama_file, index=False)
        semua_tahun_df.append(df_final_tahun)
        print(f"==> Berkas {nama_file} berhasil disimpan ({len(df_final_tahun)} baris).")

if semua_tahun_df:
    df_gabungan = pd.concat(semua_tahun_df, ignore_index=True)
    df_gabungan = df_gabungan.sort_values(by=["kode_kecamatan", "time"]).reset_index(drop=True)
    nama_excel = "dataset_cuaca_kab_sukabumi_2020_2025_sorted.xlsx"
    df_gabungan.to_excel(nama_excel, index=False)
    print(f"\n==================================================================")
    print(f"SUKSES! File Excel untuk RStudio berhasil dibuat: {nama_excel}")
    print(f"Total baris observasi: {len(df_gabungan):,} baris (47 Kecamatan, 2020-2025)")
    print(f"==================================================================")

try:
    from google.colab import files
    files.download("dataset_cuaca_kab_sukabumi_2020_2025_sorted.xlsx")
    for tahun in daftar_tahun:
        files.download(f"cuaca_kab_sukabumi_{tahun}.csv")
except ImportError:
    pass
