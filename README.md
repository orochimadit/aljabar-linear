# Matematika 2: Aljabar Linier & Geometri

<p align="center">
  <img src="logo_unukalbar.png" alt="Logo UNU Kalbar" width="120">
</p>

<p align="center">
  <strong>Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)</strong><br>
  <strong>Dosen Pengampu:</strong> Aditya Pratama<br>
  <em>Referensi Materi Akademis:</em> Rinaldi Munir (STEI ITB) & Howard Anton (<em>Elementary Linear Algebra</em>)
</p>

---

## 📖 Tentang Repositori
Repositori ini memuat perangkat ajar lengkap untuk mata kuliah **Matematika 2 (Aljabar Linier & Geometri)** pada program studi bidang teknologi informasi di **Universitas Nahdlatul Ulama Kalimantan Barat**.

Materi difokuskan pada pemahaman matematis intuitif yang dipadukan dengan implementasi komputasi praktis: Grafika Komputer, Kecerdasan Buatan (AI/LLM), Sistem Temu Balik Informasi (*Search Engine*), dan Komputasi Numerik.

---

## 📁 Struktur Repositori

```text
aljabar-linear/
│
├── 04_Slide_HTML/                           # Slide Presentasi Interaktif Berbasis Web
│   ├── index.html                           # Portal peluncur materi perkuliahan
│   ├── slide_algeo00_pengantar.html         # Slide Algeo 00 (Pengantar, Aplikasi AI, Live Canvas, Latihan)
│   ├── slide_algeo02_matriks_eselon.html    # Slide Algeo 02 (1 Utama, Sifat REF, RREF, Simulator OBE)
│   └── assets/                              # Aset logo dan video animasi tersemat
│
├── 05_Animasi_Manim/                        # Animasi Matematis Video (Engine Manim - 3Blue1Brown)
│   ├── PANDUAN_MANIM.md                     # Panduan setup FFmpeg, Manim, dan perintah render
│   ├── transformasi_geometri_2d.py          # Animasi grid transformasi linier 2D
│   ├── matriks_eselon_obe.py                # Animasi tahapan eliminasi OBE dan 1 utama (REF & RREF)
│   ├── cosine_similarity_ir.py              # Animasi visualisasi vektor kueri & dokumen pada IR
│   ├── AnimasiTransformasi2D.mp4            # Hasil render video animasi transformasi 2D
│   └── AnimasiMatriksEselon.mp4             # Hasil render video animasi matriks eselon OBE
│
├── simulasi_algeo_interaktif.py             # Aplikasi GUI Desktop Python (Tkinter + Matplotlib + NumPy)
├── LEMBAR_LATIHAN_DAN_PEMBAHASAN.md         # Bank soal latihan mahasiswa + kunci jawaban terperinci
├── PANDUAN_DAN_RANGKUMAN_MATERI.md          # Rangkuman konsep 8 bab kurikulum satu semester
├── logo_unukalbar.png                       # Berkas logo resmi UNU Kalbar
└── README.md                                # Indeks & dokumentasi utama repositori
```


---

## 🎯 Komponen Materi Pembelajaran

### 1. Slide Presentasi Web Interaktif (`04_Slide_HTML/`)
Slide perkuliahan modern tanpa memerlukan server khusus, cukup klik dua kali pada file HTML:
* **`index.html`**: Halaman depan untuk memilih modul presentasi.
* **`slide_algeo00_pengantar.html`**:
  * Motivasi mengapa mahasiswa IT wajib belajar aljabar linier.
  * 6 Pilar aplikasi nyata: Grafika 3D, Mesin Pencari, Visi Komputer, Game Quaternion, AI/LLM, dan Kuantum.
  * **Live Interactive Canvas**: Slider rotasi, skala, dan geseran (*shear*) yang mengubah arah vektor basis $\hat{i}$ dan $\hat{j}$ secara real-time di browser.
  * Contoh latihan perhitungan *Cosine Similarity* dan transformasi matriks titik grafika.
* **`slide_algeo02_matriks_eselon.html`**:
  * Konsep 1 Utama (*leading 1*), 3 Sifat Matriks Eselon Baris (REF), dan Sifat ke-4 Eselon Baris Tereduksi (RREF).
  * **Simulator Langkah OBE Live**: Tombol interaktif untuk melihat matriks acak tereliminasi baris demi baris.
  * Latihan identifikasi 8 matriks klasik dan kuis interaktif kelas.

### 2. Animasi Manim Video MP4 (`05_Animasi_Manim/`)
Animasi matematis beresolusi tinggi yang dibangun menggunakan **Manim** (engine animasi Grant Sanderson / *3Blue1Brown*):
* **`AnimasiTransformasi2D.mp4`**: Visualisasi perubahan bidang kartesius dan penskalaan luas area determinan.
* **`AnimasiMatriksEselon.mp4`**: Visualisasi langkah eliminasi matriks, penyorotan pivot hijau, dan pola tangga REF/RREF.
* Perintah render mandiri:
  ```bash
  manim -pql transformasi_geometri_2d.py AnimasiTransformasi2D
  ```

### 3. Aplikasi Simulasi Python GUI (`simulasi_algeo_interaktif.py`)
Aplikasi mandiri desktop berbasis Tkinter & Matplotlib dengan 3 tab interaktif:
* **Tab 1:** Eksplorasi animasi transformasi geometri 2D (interpolasi pergerakan grid halus).
* **Tab 2:** Solver eliminasi Gauss & Gauss-Jordan tahap demi tahap dengan log keterangan OBE.
* **Tab 3:** Visualisasi sudut kemiripan kosinus kueri terhadap dokumen pada sistem temu balik informasi (*Information Retrieval*).

Cara menjalankan:
```bash
python simulasi_algeo_interaktif.py
```

### 4. Lembar Latihan & Rangkuman Materi
* [**`LEMBAR_LATIHAN_DAN_PEMBAHASAN.md`**](LEMBAR_LATIHAN_DAN_PEMBAHASAN.md): Bahan tugas dan kuis mahasiswa yang memuat soal aplikasi komputasi, identifikasi matriks, serta eliminasi Gauss-Jordan dengan pembahasan matematis langkah demi langkah.
* [**`PANDUAN_DAN_RANGKUMAN_MATERI.md`**](PANDUAN_DAN_RANGKUMAN_MATERI.md): Silabus rangkuman 8 bab yang mencakup seluruh topik perkuliahan selama 16 minggu.

---

## 👨‍🏫 Kontak & Pengampu
* **Dosen Pengampu:** Aditya Pratama
* **Institusi:** Program Studi Informatika / Sistem Informasi, Universitas Nahdlatul Ulama Kalimantan Barat
* **Rujukan Akademis:** Rinaldi Munir (STEI ITB) & Howard Anton (*Elementary Linear Algebra*, Wiley)
