# Panduan Membuat & Me-render Animasi Aljabar Linier dengan Manim

**Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)**  
**Dosen:** Aditya Pratama  
*Engine:* **Manim (Mathematical Animation Engine)** :  Engine animasi matematika yang dipopulerkan oleh Grant Sanderson (*3Blue1Brown*).

---

##  1. Persiapan & Instalasi Cepat (Windows)

Manim membutuhkan dua komponen utama: **FFmpeg** (untuk rendering video `.mp4`) dan pustaka **manim** Python.

### Langkah 1: Pasang FFmpeg (Jalankan di PowerShell)
```powershell
winget install Gyan.FFmpeg
```
*(Setelah selesai pasang, buka jendela terminal baru agar path FFmpeg terbaca).*

### Langkah 2: Pasang Pustaka Manim Community
```bash
pip install manim
```

> **Catatan:** Sistem Anda sudah memiliki **LaTeX (MiKTeX)** terpasang, sehingga penulisan rumus matematika kompleks di video animasi akan dirender sangat tajam.

---

##  2. Koleksi Skrip Animasi Siap Pakai

Folder ini sudah dilengkapi 3 skrip animasi Manim yang diselaraskan dengan materi perkuliahan:

| Nama File | Topik Materi | Deskripsi Visual |
| :--- | :--- | :--- |
| **`transformasi_geometri_2d.py`** | Algeo 00 & Algeo 18 | Animasi grid kartesius 2D yang meliuk halus (*smooth morphing*), pergerakan vektor basis $\hat{i}$ dan $\hat{j}$, perubahan luas area unit square, serta penghitungan determinan matriks. |
| **`matriks_eselon_obe.py`** | Algeo 02 (Matriks Eselon) | Animasi matriks berubah tahap demi tahap, penyorotan *1 Utama* (*leading 1*) dengan kotak hijau menyala, eliminasi angka di bawah pivot menjadi nol (REF), hingga eliminasi atas (RREF). |
| **`cosine_similarity_ir.py`** | Algeo 00 & Algeo 14 | Animasi sumbu ruang vektor kata, vektor kueri pencarian, vektor dokumen artikel, dan visualisasi sudut kemiripan kosinus. |

---

##  3. Cara Me-render Video Animasi (.mp4)

Buka terminal/PowerShell di dalam folder `Matematika 2 - Aljabar Linear/05_Animasi_Manim/`, lalu jalankan perintah render berikut:

### A. Render Cepat untuk Preview (480p 15fps):
```bash
manim -pql transformasi_geometri_2d.py AnimasiTransformasi2D
manim -pql matriks_eselon_obe.py AnimasiMatriksEselon
manim -pql cosine_similarity_ir.py AnimasiCosineSimilarity
```
*Flag `-p` = otomatis putar video setelah selesai render.*  
*Flag `-ql` = quality low (render selesai dalam beberapa detik).*

### B. Render Kualitas Tinggi untuk Presentasi Kelas (Full HD 1080p 60fps):
```bash
manim -pqh transformasi_geometri_2d.py AnimasiTransformasi2D
```
*Video hasil render akan otomatis tersimpan dalam folder `media/videos/.../*.mp4` dan dapat langsung Anda sisipkan ke dalam slide PowerPoint atau diputar langsung di layar proyektor ruang kuliah.*
