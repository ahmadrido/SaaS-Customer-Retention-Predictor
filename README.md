# SaaS Customer Retention Predictor

## 📋 Deskripsi Proyek

Aplikasi **SaaS Customer Retention Predictor** adalah sistem prediksi berbasis machine learning yang menggunakan algoritma klasifikasi untuk memprediksi status retensi pengguna SaaS. Aplikasi ini dibangun dengan Streamlit dan membantu untuk memahami apakah seorang pengguna akan:

- **Upgrade** - Meningkatkan paket berlangganan
- **Bertahan** - Tetap menggunakan layanan dengan paket saat ini
- **Berhenti** - Membatalkan berlangganan

## 🎯 Fitur Utama

Aplikasi menganalisis perilaku pengguna berdasarkan 4 parameter kunci:

1. **Login Per Bulan** - Frekuensi login pengguna (1-30 kali)
2. **Durasi Sesi (Menit)** - Lamanya sesi pengguna menggunakan aplikasi (5-180 menit)
3. **Fitur AI yang Digunakan** - Jumlah fitur AI yang diakses pengguna (0-50)
4. **Jumlah Komplain** - Jumlah keluhan yang diajukan pengguna dalam sebulan (0-10)

## 📊 Dataset

- File: `dataset_retensi_pengguna_saas.csv`
- Berisi data historis tentang perilaku pengguna dan status retensi mereka

## 🤖 Model Machine Learning

- File: `model_pengguna_saas.joblib`
- Model telah dilatih dan siap untuk melakukan prediksi
- Menampilkan tingkat keyakinan (confidence) prediksi dalam persentase

## 🚀 Cara Menjalankan

### Prasyarat
Pastikan Python 3.7+ sudah terinstall di sistem Anda.

### Instalasi Dependensi
```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi
```bash
streamlit run main.py
```

Aplikasi akan membuka di browser default Anda pada URL `http://localhost:8501`

## 📁 Struktur File

```
machineLearning/
├── README.md                              # Dokumentasi proyek
├── requirements.txt                       # Daftar dependensi Python
├── main.py                                # File utama aplikasi Streamlit
├── model_pengguna_saas.joblib            # Model machine learning yang sudah dilatih
└── dataset_retensi_pengguna_saas.csv     # Dataset untuk training/testing
```

## 🛠️ Teknologi yang Digunakan

- **Streamlit** - Framework untuk membuat aplikasi web data science
- **Pandas** - Library untuk manipulasi dan analisis data
- **Scikit-learn** (implisit dalam model) - Library machine learning
- **Joblib** - Serialisasi dan penyimpanan model Python

## 📈 Cara Kerja Aplikasi

1. Pengguna memasukkan nilai 4 parameter perilaku pengguna melalui interface slider
2. Data yang dimasukkan diproses oleh model machine learning
3. Model memberikan prediksi status retensi pengguna
4. Aplikasi menampilkan hasil dengan warna yang berbeda:
   - **Hijau** (Upgrade) - Pengguna akan upgrade
   - **Biru** (Bertahan) - Pengguna akan tetap bertahan
   - **Merah** (Berhenti) - Peringatan pengguna berisiko berhenti

## 💡 Use Case

Aplikasi ini dapat digunakan untuk:
- Mengidentifikasi pengguna yang berisiko churn (berhenti berlangganan)
- Memprioritaskan pengguna untuk campaign retensi
- Mengidentifikasi peluang upsell (upgrade)
- Menganalisis pola perilaku pengguna SaaS

## 📝 Catatan

- Model ini didasarkan pada data historis pengguna SaaS
- Akurasi prediksi tergantung pada kualitas dan relevansi data training
- Tingkat keyakinan ditampilkan untuk setiap prediksi

## 👨‍💻 Pengembangan Lebih Lanjut

Beberapa ide untuk pengembangan:
- Menambahkan fitur analitik dashboard
- Mengintegrasikan dengan database untuk menyimpan riwayat prediksi
- Menambahkan fitur export laporan
- Melatih ulang model dengan data terbaru secara berkala

---

**Dibuat dengan ❤️ menggunakan Streamlit**
