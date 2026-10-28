# Desain & Identitas Visual: Aljabar Linier & Geometri

Dokumen ini memuat panduan identitas visual dan token desain untuk materi perkuliahan Matematika 2 (Aljabar Linier & Geometri) di lingkungan Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar).

---

## 1. Dials (Pengaturan Karakter UI)

- **ENERGY: 1** (Tenang, akademis, fokus pada keterbacaan rumus dan diagram)
- **RHYTHM: 2** (Hierarki jelas: judul bab, definisi formal, visualisasi grafis/matriks, latihan terstruktur)
- **MOTION: 1** (Fungsional: animasi hanya dipakai untuk mendemonstrasikan transformasi geometri dan langkah eliminasi baris, bukan hiasan transisi)

---

## 2. Palet Warna (UNU Kalbar Academic Slate & Emerald)

Palet dirancang berbasis tema gelap kontras tinggi untuk kenyamanan proyeksi di ruang kuliah dan layar komputer:

- **Latar Belakang Utama**: `#0b1120` (Slate 950)
- **Permukaan Kartu / Kontainer**: `#151e32` (Slate 900)
- **Garis Batas (Border)**: `#24324d` (Slate 800)
- **Warna Identitas Primer (UNU Green)**: `#059669` / `#10b981` (Emerald 600/500)
- **Warna Aksen Vektor / Pivot (Akademis)**: `#38bdf8` (Sky 400)
- **Warna Sorotan Status / Evaluasi**: `#d97706` / `#f59e0b` (Amber 600/500)
- **Teks Utama**: `#f8fafc` (Slate 50, rasio kontras > 14:1 terhadap latar)
- **Teks Sekunder / Keterangan**: `#cbd5e1` (Slate 300, rasio kontras > 7:1 terhadap latar)
- **Teks Nonaktif / Catatan**: `#94a3b8` (Slate 400, rasio kontras > 4.5:1 terhadap latar)

---

## 3. Tipografi

- **Teks Utama & Heading**: System Sans-Serif (`system-ui`, `-apple-system`, `"Segoe UI"`, `Roboto`, `Helvetica Neue`, `sans-serif`)
  - Keterbacaan tinggi, bersih, tanpa hiasan berlebih.
- **Notasi Matriks & Kode**: Monospace (`"Consolas"`, `"Courier New"`, `monospace`)
  - Digunakan khusus untuk representasi matriks siku, langkah OBE, dan blok skrip komputasi Python.

---

## 4. Prinsip Komposisi & Anti-Slop

1. **Bebas Em Dash**: Dilarang menggunakan karakter em dash (tanda pisah panjang); gunakan tanda titik dua (`:`), tanda hubung (`-`), koma (`,`), atau tanda kurung `()`.
2. **Bebas Polusi Emoji**: Simbol visual digantikan dengan tipografi formal, nomor urut terstruktur, atau notasi matematika standar.
3. **Bebas Gelar pada Penamaan Pengampu & Referensi**: Cukup gunakan nama `"Aditya Pratama"` dan `"Rinaldi Munir"`.
4. **Fungsionalitas Penuh**: Setiap tombol dan input wajib memiliki aksi komputasi nyata.

---

## 5. Standar Desain Hallmark (The Floor)

Seluruh antarmuka web perkuliahan divalidasi dengan Hallmark Anti-Slop Linter (`sloplint.mjs`):
1. **CSS Stamp & Token Block**: Semua warna dan font dideklarasikan di blok token `:root` berbasis OKLCH/sistem, tanpa nilai literal mentah pada aturan selektor.
2. **Kepatuhan Transisi**: Menghindari `transition: all` dan transisi `width`/`height`. Semua transisi dideklarasikan spesifik pada `transform` atau `opacity`.
3. **Aksesibilitas & Reduksi Gerak**: Elemen interaktif dilengkapi ring `:focus-visible` instan berkontras tinggi dan kueri media `@media (prefers-reduced-motion: reduce)`.
4. **Bebas Eyebrow & Tracked Capitals**: Menghilangkan label kapital spasi renggang di atas heading utama untuk menjaga keanggunan tipografi editorial.
5. **Kerapian Tata Letak Responsif**: Menerapkan `overflow-x: clip` pada `html` dan `body` untuk mengeliminasi potensi pergeseran horizontal.
