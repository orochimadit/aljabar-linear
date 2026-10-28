# Matematika 2 / Aljabar Linier dan Geometri

**Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)**  
**Dosen Pengampu:** Aditya Pratama  
*Referensi Akademis Utama:* Rinaldi Munir dkk. (STEI ITB) & Howard Anton (*Elementary Linear Algebra*).

---

## 📁 Struktur Direktori

```text
Matematika 2 - Aljabar Linear/
│
├── 00_Silabus_dan_Informasi/
│   ├── Info-Algeo-2026.pdf                 # Informasi silabus, bobot nilai, aturan perkuliahan
│   └── RencanaKuliah2026.pdf               # Jadwal per minggu & topik pertemuan semester 1
│
├── 01_Materi_Slide/
│   ├── Algeo-00-Pengantar-Aljabar-Geometri-(2026).pdf
│   ├── Algeo-01-Review-Matriks-2025.pdf
│   ├── Algeo-02-Matriks-Eselon-2025.pdf
│   ├── Algeo-03-Sistem-Persamaan-Linier-2025.pdf
│   ├── Algeo-04-Tiga-Kemungkinan-Solusi-SPL-2025.pdf
│   ├── Algeo-05-Sistem-Persamaan-Linier-2-2025.pdf
│   ├── Algeo-06-Aplikasi-SPL-1-2025.pdf
│   ├── Algeo-07-Aplikasi-SPL-2-2025.pdf
│   ├── Algeo-08-Determinan-bagian1-2025.pdf
│   ├── Algeo-09-Determinan-bagian2-2025.pdf
│   ├── Algeo-10-Pengantar-Pemrograman-dengan-Bahasa-Java-2026.pdf
│   ├── Algeo-11-Vektor-di-Ruang-Euclidean-Bag1-2025.pdf
│   ├── Algeo-12-Vektor-di-Ruang-Euclidean-Bag2-2025.pdf
│   ├── Algeo-13-Vektor-di-Ruang-Euclidean-Bag3-2025.pdf
│   ├── Algeo-14-Aplikasi-dot-product-pada-IR-2025.pdf
│   ├── Algeo-15-Ruang-vektor-umum-Bagian1-2025.pdf
│   ├── Algeo-16-Ruang-vektor-umum-Bagian2-2025.pdf
│   ├── Algeo-17-Ruang-vektor-umum-Bagian3-2025.pdf
│   ├── Algeo-18-Ruang-vektor-umum-Bagian4-2025.pdf
│   ├── Algeo-19-Nilai-Eigen-dan-Vektor-Eigen-Bagian1-2025.pdf
│   ├── Algeo-20-Nilai-Eigen-dan-Vektor-Eigen-Bagian2-2025.pdf
│   ├── Algeo-21-Singular-value-decomposition-Bagian1-2025.pdf
│   ├── Algeo-22-Singular-value-decomposition-Bagian2-2025.pdf
│   ├── Algeo-23-Dekomposisi-LU-2025.pdf
│   └── Algeo-24-Dekomposisi-QR-2025.pdf
│
├── 02_Kuis_dan_Ujian/
│   ├── Kuis-1-IF2123-2026.pdf               # Kuis SPL & Determinan
│   ├── Solusi-Kuis-1-IF2123-2026.pdf        # Pembahasan Kuis 1
│   ├── Kuis-2-IF2123-2026.pdf               # Kuis Vektor Euclidean & Ruang Vektor
│   ├── Solusi-Kuis-2-IF2123-2026.pdf        # Pembahasan Kuis 2
│   ├── UTS-IF2123-Algeo-2025 (Referensi Latihan).pdf
│   ├── Solusi-UTS-IF2123-Algeo-2025 (Referensi Latihan).pdf
│   └── UTS-IF2123-Algeo-2024 (Referensi Latihan).pdf
│
├── 03_Tugas_Besar/
│   └── Tubes1-Algeo-2026.pdf                # Spesifikasi Tubes 1 (SPL, Determinan, Spline, Java)
│
├── 04_Slide_HTML/
│   ├── index.html                           # Portal peluncur slide presentasi interaktif
│   ├── slide_algeo00_pengantar.html         # Slide Algeo 00 (Pengantar, Aplikasi IT, Live Canvas, Contoh Latihan)
│   └── slide_algeo02_matriks_eselon.html    # Slide Algeo 02 (1 Utama, Sifat REF, RREF, Simulator OBE, Latihan 8 Matriks)
│
├── 05_Animasi_Manim/
│   ├── PANDUAN_MANIM.md                     # Panduan instalasi FFmpeg, Manim, dan perintah render
│   ├── transformasi_geometri_2d.py          # Animasi grid transformasi linier 2D gaya 3Blue1Brown
│   ├── matriks_eselon_obe.py                # Animasi tahapan eliminasi OBE dan 1 utama menuju REF & RREF
│   └── cosine_similarity_ir.py              # Animasi visualisasi vektor kueri & dokumen pada IR System
│
├── simulasi_algeo_interaktif.py             # Aplikasi GUI simulasi Python desktop (Tkinter + Matplotlib)
├── LEMBAR_LATIHAN_DAN_PEMBAHASAN.md         # Lembar soal latihan mandiri & pembahasan lengkap per bab
├── PANDUAN_DAN_RANGKUMAN_MATERI.md          # Rangkuman konsep, rumus, dan algoritma penting
└── README.md                                # Dokumen indeks ini
```

---

## 🐍 Cara Menjalankan Aplikasi Simulasi Python

Buka terminal / PowerShell di folder ini, lalu jalankan:
```bash
python "Matematika 2 - Aljabar Linear/simulasi_algeo_interaktif.py"
```
Fitur yang tersedia dalam aplikasi simulasi:
1. **Tab 1: Animasi Transformasi Geometri 2D** (Visualisasi rotasi, penskalaan, dan geseran vektor basis secara halus).
2. **Tab 2: Simulator Langkah Eliminasi Gauss & Gauss-Jordan** (Animasi pembentukan 1 Utama dan eliminasi nol bertahap).
3. **Tab 3: Simulasi Cosine Similarity pada Mesin Pencari** (Eksplorasi sudut kosinus kueri terhadap vektor dokumen).
│
├── 03_Tugas_Besar/
│   └── Tubes1-Algeo-2026.pdf                # Spesifikasi Tubes 1 (SPL, Determinan, Spline, Java)
│
├── 04_Slide_HTML/
│   ├── index.html                           # Portal peluncur slide presentasi interaktif
│   ├── slide_algeo00_pengantar.html         # Slide Algeo 00 (Pengantar, Aplikasi IT, Roadmap, Tubes)
│   └── slide_algeo02_matriks_eselon.html    # Slide Algeo 02 (1 Utama, Sifat REF, RREF, Kuis Interaktif)
│
├── PANDUAN_DAN_RANGKUMAN_MATERI.md          # Rangkuman konsep, rumus, dan algoritma penting
└── README.md                                # Dokumen indeks ini
```

---

## 🎯 Ringkasan Komponen Mata Kuliah

1. **Komputasi Matriks & SPL**
   - Operasi Baris Elementer (OBE)
   - Eliminasi Gauss & Eliminasi Gauss-Jordan
   - Tiga kemungkinan solusi SPL: Solusi Unik, Solusi Banyak (parametrik), Tidak Ada Solusi (inkonsisten)
   - Determinan: Reduksi Baris, Ekspansi Kofaktor
   - Matriks Balikan (Invers) dengan OBE $[A | I] \to [I | A^{-1}]$ dan Matriks Adjoin.

2. **Ruang Vektor (Vector Spaces)**
   - Ruang Euclidean $\mathbb{R}^n$ (norma, dot product, sudut, orthogonalitas, proyeksi vektor, cross product)
   - Ruang Vektor Umum (10 aksioma ruang vektor, subruang)
   - Kombinasi Linier, Rentang (Span), Bebas Linier (Linear Independence)
   - Basis dan Dimensi, Ruang Baris, Ruang Kolom, Ruang Nol (Nullspace), Teorema Rank-Nullity
   - Transformasi Linier dan Representasi Matriks

3. **Spektral & Dekomposisi Matriks Lanjut**
   - Nilai Eigen & Vektor Eigen, Persamaan Karakteristik $\det(\lambda I - A) = 0$
   - Diagonalisasi Matriks ($A = P D P^{-1}$) & Diagonalisasi Ortogonal matriks simetris
   - Singular Value Decomposition (SVD: $A = U \Sigma V^T$) & Kompresi Citra / Reduksi Dimensi
   - Dekomposisi LU ($A = LU$) dan Solusi SPL Efisien
   - Dekomposisi QR ($A = QR$) melalui Proses Gram-Schmidt

4. **Aplikasi Nyata di Bidang Informatika**
   - *Information Retrieval* (Sistem Temu Kembali Informasi menggunakan Cosine Similarity pada model Vector Space)
   - Interpolasi Polinomial & Natural Cubic Spline Interpolation
   - Regresi Spline
   - *Image Inpainting* menggunakan Persamaan Laplace
   - Jaringan Aliran Listrik (Hukum Kirchhoff) dan Aliran Lalu Lintas
