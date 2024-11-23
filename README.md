# 📊 E-Commerce Dashboard Analysis  

## 📖 Deskripsi  
Proyek ini adalah dashboard interaktif yang dirancang untuk menganalisis data e-commerce, termasuk tren penjualan, kategori produk, ulasan pelanggan, durasi pengiriman, dan proporsi tipe pembayaran. Dashboard ini dapat membantu dalam pengambilan keputusan bisnis.  

## 🎯 Fitur Utama  
- **Analisis Penjualan Bulanan**: Menampilkan tren penjualan secara bulanan.  
- **Kategori Produk Terpopuler**: Mengidentifikasi 10 kategori produk teratas berdasarkan jumlah penjualan.  
- **Durasi Pengiriman**: Distribusi waktu pengiriman dan korelasinya dengan ulasan pelanggan.  
- **Skor Ulasan Pelanggan**: Distribusi skor ulasan.  
- **Pendapatan Berdasarkan Kategori**: Mengidentifikasi kategori produk dengan pendapatan tertinggi.  
- **Proporsi Tipe Pembayaran**: Distribusi metode pembayaran yang digunakan pelanggan.  

## 🛠️ Persyaratan  
- **Python** (versi 3.11 atau lebih baru)
- **pip** (manajer paket Python)

### 🗂️ Library yang Dibutuhkan  
- `streamlit`
- `pandas`
- `numpy`
- `plotly`

## 🚀 Setup Environment  

1. **Clone Repository**  
   Clone repository ini ke komputer lokal:
   ```bash
   git clone https://github.com/username/ecommerce-dashboard.git
   cd ecommerce-dashboard
   ```

2. **Buat Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install Dependencies**  
   Jalankan perintah berikut untuk menginstal semua library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

4. **Dataset**  
   Pastikan file dataset `merged_data_ecommerce.csv` berada di direktori utama proyek.

## ▶️ Cara Menjalankan Dashboard  
1. Jalankan aplikasi Streamlit menggunakan perintah berikut:
   ```bash
   streamlit run app.py
   ```
2. Buka browser Anda dan akses URL yang diberikan, biasanya:
   ```
   http://localhost:8501
   ```

## 📊 Data yang Digunakan  
Dataset yang digunakan berisi informasi terkait transaksi e-commerce seperti:
- **Kolom Utama**:
  - `order_purchase_timestamp`: Waktu pembelian.
  - `product_category_name_english`: Kategori produk dalam bahasa Inggris.
  - `customer_state`: Lokasi pembeli berdasarkan provinsi.
  - `review_score`: Skor ulasan pelanggan (1-5).
  - `delivery_time`: Durasi pengiriman (hari).
  - `price`: Harga produk.
  - `payment_type`: Metode pembayaran.

## 📄 Struktur Proyek  
Struktur direktori proyek:
```
ecommerce-dashboard/
│
├── app.py               # File utama untuk menjalankan dashboard
├── merged_data_ecommerce.csv  # Dataset
├── requirements.txt     # Daftar pustaka yang dibutuhkan
└── README.md            # Dokumentasi proyek
```

## 📜 Catatan  
- Jika terjadi masalah saat menjalankan aplikasi, periksa kembali library yang telah diinstal dan pastikan dataset sudah tersedia di direktori yang benar.
