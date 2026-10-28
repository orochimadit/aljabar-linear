# Lembar Latihan & Pembahasan: Aljabar Linier & Geometri

**Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)**  
**Dosen Pengampu:** Aditya Pratama  
*Diadaptasi dari kumpulan soal latihan:* Rinaldi Munir (STEI ITB) & Howard Anton (*Elementary Linear Algebra*).

---

## Bagian 1: Latihan Algeo 00 (Aplikasi Komputasi Aljabar Linier)

### Soal 1.1: Pemodelan Information Retrieval & Cosine Similarity
Sebuah sistem temu balik informasi (*search engine*) sederhana menggunakan model ruang vektor (*Vector Space Model*) untuk memeringkat relevansi artikel berita.
Diberikan representasi vektor kueri pencarian $Q$ dan tiga dokumen artikel dalam basis data berdasarkan frekuensi kemunculan dua kata kunci ("Kecerdasan" dan "Artifisial"):
* Vektor Kueri: $Q = (3, 4)$
* Dokumen 1: $D_1 = (6, 8)$
* Dokumen 2: $D_2 = (1, 7)$
* Dokumen 3: $D_3 = (5, 0)$

**Pertanyaan:**
1. Hitung panjang (norma Euclidean) dari masing-masing vektor.
2. Hitung nilai kemiripan sudut (*Cosine Similarity*) antara $Q$ dengan masing-masing dokumen.
3. Urutkan dokumen dari yang paling relevan hingga yang paling tidak relevan.

#### Pembahasan Soal 1.1:
1. **Panjang Norma Euclidean ($\|V\| = \sqrt{x^2 + y^2}$):**
   * $\|Q\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$
   * $\|D_1\| = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$
   * $\|D_2\| = \sqrt{1^2 + 7^2} = \sqrt{1 + 49} = \sqrt{50} = 5\sqrt{2} \approx 7.071$
   * $\|D_3\| = \sqrt{5^2 + 0^2} = 5$

2. **Perhitungan Kemiripan Kosinus ($\cos \theta = \frac{Q \cdot D}{\|Q\| \|D\|}$):**
   * **Dokumen 1:**
     $$Q \cdot D_1 = (3)(6) + (4)(8) = 18 + 32 = 50$$
     $$\cos \theta_1 = \frac{50}{(5)(10)} = \frac{50}{50} = \mathbf{1.0} \quad (\theta = 0^\circ, \text{kemiripan } 100\%)$$
   * **Dokumen 2:**
     $$Q \cdot D_2 = (3)(1) + (4)(7) = 3 + 28 = 31$$
     $$\cos \theta_2 = \frac{31}{(5)(5\sqrt{2})} = \frac{31}{25\sqrt{2}} \approx \frac{31}{35.355} \approx \mathbf{0.8768} \quad (\text{kemiripan } 87.7\%)$$
   * **Dokumen 3:**
     $$Q \cdot D_3 = (3)(5) + (4)(0) = 15$$
     $$\cos \theta_3 = \frac{15}{(5)(5)} = \frac{15}{25} = \mathbf{0.6} \quad (\text{kemiripan } 60\%)$$

3. **Urutan Peringkat Relevansi:**
   $$\text{Peringkat 1: } D_1 \; (1.0) \;\; > \;\; \text{Peringkat 2: } D_2 \; (0.8768) \;\; > \;\; \text{Peringkat 3: } D_3 \; (0.6)$$

---

### Soal 1.2: Transformasi Matriks 2D Objek Grafika
Sebuah titik poligon $P(4, 2)$ pada layar monitor akan diproses oleh pipa grafika dengan urutan sebagai berikut:
1. Diputar $90^\circ$ berlawanan arah jarum jam dengan matriks rotasi $R_{90^\circ} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.
2. Hasil rotasi diskalakan 3 kali lipat dengan matriks skala $S = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$.

**Pertanyaan:**
1. Tentukan matriks transformasi gabungan $T = S \cdot R_{90^\circ}$.
2. Tentukan koordinat titik akhir $P''$.

#### Pembahasan Soal 1.2:
1. **Perkalian Matriks Transformasi Gabungan $T$:**
   $$T = S \cdot R_{90^\circ} = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} (3)(0)+0 & (3)(-1)+0 \\ 0+(3)(1) & 0+(3)(0) \end{bmatrix} = \begin{bmatrix} 0 & -3 \\ 3 & 0 \end{bmatrix}$$
2. **Koordinat Titik Akhir $P''$:**
   $$P'' = T \cdot P = \begin{bmatrix} 0 & -3 \\ 3 & 0 \end{bmatrix} \begin{bmatrix} 4 \\ 2 \end{bmatrix} = \begin{bmatrix} (0)(4) + (-3)(2) \\ (3)(4) + (0)(2) \end{bmatrix} = \begin{bmatrix} -6 \\ 12 \end{bmatrix}$$
   Titik akhir berada pada koordinat $(-6, 12)$.

---

## Bagian 2: Latihan Algeo 02 (Matriks Eselon Baris & Tereduksi)

### Soal 2.1: Klasifikasi Status Bentuk Matriks
Tentukan apakah matriks-matriks di bawah ini merupakan:
- **(i)** Matriks Eselon Baris (REF saja)
- **(ii)** Matriks Eselon Baris Tereduksi (RREF / Keduanya)
- **(iii)** Bukan Keduanya (Jelaskan sifat yang dilanggar)

1. $A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
2. $B = \begin{bmatrix} 1 & 4 & -2 & 3 \\ 0 & 1 & 0 & 7 \\ 0 & 0 & 1 & 1 \end{bmatrix}$
3. $C = \begin{bmatrix} 1 & 0 & 0 & 4 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 3 \end{bmatrix}$
4. $D = \begin{bmatrix} 1 & 2 & 0 & 5 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
5. $E = \begin{bmatrix} 2 & 3 & 1 \\ 0 & 1 & 4 \\ 0 & 0 & 1 \end{bmatrix}$
6. $F = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 2 \end{bmatrix}$
7. $G = \begin{bmatrix} 1 & 3 & 5 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$
8. $H = \begin{bmatrix} 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$

#### Pembahasan Soal 2.1:
1. **Matriks $A$:** **Keduanya (REF & RREF)**. Ini adalah matriks identitas $I_3$. Setiap kolom yang memuat 1 utama memiliki nilai nol di semua entri lainnya.
2. **Matriks $B$:** **Hanya REF**. Di atas 1 utama baris 2 (kolom 2) terdapat angka 4, dan di atas 1 utama baris 3 (kolom 3) terdapat angka $-2$ dan $0$. Belum nol bersih di atas 1 utama, sehingga bukan RREF.
3. **Matriks $C$:** **Keduanya (REF & RREF)**. Kolom 1, 2, dan 3 memuat 1 utama dan seluruh entri lain di kolom tersebut bernilai 0. Kolom 4 berisi angka sembarang tidak masalah karena kolom 4 bukan kolom 1 utama.
4. **Matriks $D$:** **Keduanya (REF & RREF)**. Baris nol di dasar matriks. Kolom 1 memuat 1 utama (bersih nol). Kolom 3 memuat 1 utama (bersih nol). Kolom 2 dan 4 bukan kolom 1 utama.
5. **Matriks $E$:** **Bukan Keduanya**. Elemen bukan-nol pertama pada baris 1 adalah angka **2** (bukan 1 utama). Melanggar Sifat 1 REF.
6. **Matriks $F$:** **Bukan Keduanya**. Baris nol berada pada baris 2, sementara baris 3 bukan nol. Baris nol wajib berada di paling bawah matriks. Melanggar Sifat 2 REF.
7. **Matriks $G$:** **Bukan Keduanya**. 1 utama baris 2 terletak pada kolom 3, sedangkan 1 utama baris 3 terletak pada kolom 2 (lebih ke kiri). Melanggar Sifat 3 (pola tangga terbalik).
8. **Matriks $H$:** **Keduanya (REF & RREF)**. Kolom 2 memiliki 1 utama di baris 1 (bersih nol). Kolom 4 memiliki 1 utama di baris 2 (bersih nol). Kolom 1 dan 3 bukan kolom 1 utama.

---

### Soal 2.2: Praktik Operasi Baris Elementer (OBE)
Diberikan matriks $M$:
$$M = \begin{bmatrix}
2 & 4 & -2 & \bigm| & 6 \\
1 & 3 & 4 & \bigm| & 2 \\
5 & 2 & -1 & \bigm| & 7
\end{bmatrix}$$

**Tugas:**
1. Lakukan Eliminasi Gauss untuk mengubah matriks $M$ menjadi bentuk **Eselon Baris (REF)**.
2. Lanjutkan dengan Eliminasi Gauss-Jordan untuk mengubahnya menjadi bentuk **Eselon Baris Tereduksi (RREF)**.
3. Tuliskan nilai solusi unik $(x_1, x_2, x_3)$ yang diperoleh.

#### Pembahasan Soal 2.2:

* **Tahap 1: Membentuk 1 Utama Baris 1**
  Operasi: $R_1 \leftarrow \frac{1}{2} R_1$
  $$M_1 = \begin{bmatrix}
  \mathbf{1} & 2 & -1 & \bigm| & 3 \\
  1 & 3 & 4 & \bigm| & 2 \\
  5 & 2 & -1 & \bigm| & 7
  \end{bmatrix}$$

* **Tahap 2: Nol-kan Kolom 1 di Bawah 1 Utama**
  Operasi: $R_2 \leftarrow R_2 - R_1$ dan $R_3 \leftarrow R_3 - 5R_1$
  $$R_2: [1-1 \quad 3-2 \quad 4-(-1) \bigm| 2-3] = [0 \quad 1 \quad 5 \bigm| -1]$$
  $$R_3: [5-5 \quad 2-10 \quad -1-(-5) \bigm| 7-15] = [0 \quad -8 \quad 4 \bigm| -8]$$
  $$M_2 = \begin{bmatrix}
  \mathbf{1} & 2 & -1 & \bigm| & 3 \\
  0 & \mathbf{1} & 5 & \bigm| & -1 \\
  0 & -8 & 4 & \bigm| & -8
  \end{bmatrix}$$

* **Tahap 3: Nol-kan Kolom 2 di Bawah 1 Utama Baris 2**
  Operasi: $R_3 \leftarrow R_3 + 8R_2$
  $$R_3: [0+0 \quad -8+8 \quad 4 + 8(5) \bigm| -8 + 8(-1)] = [0 \quad 0 \quad 44 \bigm| -16]$$
  $$M_3 = \begin{bmatrix}
  \mathbf{1} & 2 & -1 & \bigm| & 3 \\
  0 & \mathbf{1} & 5 & \bigm| & -1 \\
  0 & 0 & 44 & \bigm| & -16
  \end{bmatrix}$$

* **Tahap 4: Membentuk 1 Utama Baris 3 -> Bentuk REF Tercapai**
  Operasi: $R_3 \leftarrow \frac{1}{44} R_3$
  $$M_{\text{REF}} = \begin{bmatrix}
  \mathbf{1} & 2 & -1 & \bigm| & 3 \\
  0 & \mathbf{1} & 5 & \bigm| & -1 \\
  0 & 0 & \mathbf{1} & \bigm| & -\frac{4}{11}
  \end{bmatrix}$$
  **Status: Matriks Eselon Baris (REF) telah terpenuhi.**

* **Tahap 5: Gauss-Jordan Menuju RREF (Nol-kan di Atas 1 Utama)**
  - Nol-kan kolom 3:
    $R_2 \leftarrow R_2 - 5R_3 \implies R_2 = [0 \quad 1 \quad 0 \bigm| -1 - 5(-\frac{4}{11}) = \frac{9}{11}]$
    $R_1 \leftarrow R_1 + R_3 \implies R_1 = [1 \quad 2 \quad 0 \bigm| 3 + (-\frac{4}{11}) = \frac{29}{11}]$
  - Nol-kan kolom 2 baris 1:
    $R_1 \leftarrow R_1 - 2R_2 \implies R_1 = [1 \quad 0 \quad 0 \bigm| \frac{29}{11} - 2(\frac{9}{11}) = \frac{11}{11} = 1]$

  $$M_{\text{RREF}} = \begin{bmatrix}
  \mathbf{1} & 0 & 0 & \bigm| & 1 \\
  0 & \mathbf{1} & 0 & \bigm| & \frac{9}{11} \\
  0 & 0 & \mathbf{1} & \bigm| & -\frac{4}{11}
  \end{bmatrix}$$

* **Hasil Solusi SPL:**
  $$x_1 = 1, \quad x_2 = \frac{9}{11}, \quad x_3 = -\frac{4}{11}$$

---

*Disusun khusus untuk materi ajar mahasiswa Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar).*
