# Panduan Belajar & Rangkuman Komprehensif: Aljabar Linier & Geometri

**Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)**  
**Dosen Pengampu:** Aditya Pratama  
*Diadaptasi dengan rujukan materi akademis utama:* Rinaldi Munir (STEI ITB) & Howard Anton (*Elementary Linear Algebra*).

---

## DAFTAR ISI
1. [Bagian 1: Matriks, Operasi Baris Elementer, dan Bentuk Eselon](#bagian-1-matriks-operasi-baris-elementer-dan-bentuk-eselon)
2. [Bagian 2: Sistem Persamaan Linier (SPL)](#bagian-2-sistem-persamaan-linier-spl)
3. [Bagian 3: Determinan dan Invers Matriks](#bagian-3-determinan-dan-invers-matriks)
4. [Bagian 4: Vektor di Ruang Euclidean & Information Retrieval](#bagian-4-vektor-di-ruang-euclidean--information-retrieval)
5. [Bagian 5: Ruang Vektor Umum, Basis, dan Dimensi](#bagian-5-ruang-vektor-umum-basis-dan-dimensi)
6. [Bagian 6: Nilai Eigen, Vektor Eigen, dan Diagonalisasi](#bagian-6-nilai-eigen-vektor-eigen-dan-diagonalisasi)
7. [Bagian 7: Dekomposisi Matriks (SVD, LU, QR)](#bagian-7-dekomposisi-matriks-svd-lu-qr)
8. [Bagian 8: Penerapan Praktis & Persiapan Tugas Besar 1](#bagian-8-penerapan-praktis--persiapan-tugas-besar-1)

---

## Bagian 1: Matriks, Operasi Baris Elementer, dan Bentuk Eselon

### 1.1 Jenis-jenis Matriks Khusus
- **Matriks Nol ($O$)**: Semua elemennya bernilai 0.
- **Matriks Satuan/Identitas ($I_n$)**: Matriks persegi dengan diagonal utama bernilai 1 dan elemen lainnya bernilai 0.
- **Matriks Diagonal**: Matriks persegi dengan elemen di luar diagonal utama bernilai 0 ($a_{ij} = 0$ untuk $i \neq j$).
- **Matriks Segitiga Atas (*Upper Triangular*)**: $a_{ij} = 0$ untuk $i > j$.
- **Matriks Segitiga Bawah (*Lower Triangular*)**: $a_{ij} = 0$ untuk $i < j$.
- **Matriks Simetris**: $A^T = A$. Matriks *skew-symmetric*: $A^T = -A$.
- **Matriks Ortogonal**: $A^T A = A A^T = I$, sehingga $A^{-1} = A^T$.

### 1.2 Tiga Operasi Baris Elementer (OBE)
Operasi Baris Elementer mempertahankan himpunan solusi dari suatu sistem persamaan linier:
1. **Pertukaran Baris**: $R_i \leftrightarrow R_j$ (menukar baris ke-$i$ dengan baris ke-$j$).
2. **Perkalian Skalar**: $R_i \leftarrow k R_i$ dengan $k \neq 0$ (mengalikan baris ke-$i$ dengan skalar bukan nol).
3. **Penjumlahan Baris Kelipatan**: $R_i \leftarrow R_i + c R_j$ (menambahkan kelipatan baris ke-$j$ ke baris ke-$i$).

### 1.3 Matriks Eselon Baris (Row Echelon Form - REF)
Matriks berukuran $m \times n$ berada dalam bentuk eselon baris jika:
1. Jika suatu baris tidak seluruhnya nol, angka bukan nol pertama dalam baris tersebut adalah 1 (*leading 1* / 1 utama).
2. Jika ada baris yang seluruhnya nol, baris tersebut diletakkan di bagian paling bawah matriks.
3. Untuk setiap dua baris tak nol berurutan, 1 utama pada baris yang lebih bawah berada lebih ke kanan daripada 1 utama pada baris di atasnya.

### 1.4 Matriks Eselon Baris Tereduksi (Reduced Row Echelon Form - RREF)
Memenuhi syarat bentuk eselon baris, ditambah:
- Setiap kolom yang memuat 1 utama memiliki angka 0 di setiap entri lainnya pada kolom tersebut.

---

## Bagian 2: Sistem Persamaan Linier (SPL)

Bentuk umum SPL dengan $m$ persamaan dan $n$ variabel:
$$A x = b$$
Matriks *augmented* (matriks diperbesar):
$$[A \mid b] = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} & \bigm| & b_1 \\
a_{21} & a_{22} & \dots & a_{2n} & \bigm| & b_2 \\
\vdots & \vdots & \ddots & \vdots & \bigm| & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn} & \bigm| & b_m
\end{bmatrix}$$

### 2.1 Metode Penyelesaian
1. **Eliminasi Gauss**: Mengubah $[A \mid b]$ menjadi bentuk Eselon Baris (REF), lalu melakukan substitusi balik (*back-substitution*).
2. **Eliminasi Gauss-Jordan**: Mengubah $[A \mid b]$ menjadi bentuk Eselon Baris Tereduksi (RREF), sehingga nilai peubah dapat langsung dibaca tanpa substitusi balik.
3. **Metode Matriks Balikan**: Jika $A$ persegi ($n \times n$) dan invertible ($\det(A) \neq 0$), maka $x = A^{-1} b$.
4. **Kaidah Cramer**: Menggunakan determinan:
   $$x_j = \frac{\det(A_j)}{\det(A)}$$
   di mana $A_j$ adalah matriks $A$ yang kolom ke-$j$ diganti dengan vektor $b$.

### 2.2 Tiga Kemungkinan Solusi SPL
- **Solusi Unik (Tunggal)**: Terjadi jika $\text{rank}(A) = \text{rank}([A \mid b]) = n$ (jumlah peubah). Bentuk eselon memiliki 1 utama pada setiap kolom peubah.
- **Solusi Banyak (Tak Terhingga)**: Terjadi jika $\text{rank}(A) = \text{rank}([A \mid b]) = r < n$. Terdapat $n - r$ variabel bebas (*free variables*) yang dinyatakan dalam parameter skalar ($s, t, \dots$).
- **Tidak Ada Solusi (Inkonsisten)**: Terjadi jika $\text{rank}(A) < \text{rank}([A \mid b])$, yang ditandai dengan munculnya baris berbentuk $[0 \; 0 \; \dots \; 0 \mid c]$ di mana $c \neq 0$.

---

## Bagian 3: Determinan dan Invers Matriks

### 3.1 Metode Perhitungan Determinan
1. **Reduksi Baris (Menuju Segitiga Atas/Bawah)**:
   - Jika matriks segitiga, $\det(A) = \prod_{i=1}^n a_{ii}$ (hasil kali elemen diagonal utama).
   - Efek OBE terhadap determinan:
     - Menukar dua baris: determinan dikalikan $-1$.
     - Mengalikan satu baris dengan $k$: determinan dikalikan $k$.
     - Menambahkan kelipatan baris lain: determinan **tidak berubah**.
2. **Ekspansi Kofaktor (Teorema Laplace)**:
   - Minor $M_{ij}$: Determinan submatriks yang diperoleh dengan menghapus baris ke-$i$ dan kolom ke-$j$.
   - Kofaktor $C_{ij} = (-1)^{i+j} M_{ij}$.
   - Ekspansi sepanjang baris ke-$i$: $\det(A) = \sum_{j=1}^n a_{ij} C_{ij}$.
   - Ekspansi sepanjang kolom ke-$j$: $\det(A) = \sum_{i=1}^n a_{ij} C_{ij}$.

### 3.2 Menghitung Matriks Balikan (Invers)
- **Metode OBE Gauss-Jordan**:
  $$[A \mid I] \xrightarrow{\text{OBE}} [I \mid A^{-1}]$$
  Jika ruas kiri tidak dapat diubah menjadi $I$, maka $A$ tidak memiliki invers (matriks singular).
- **Metode Adjoin Matriks**:
  $$\text{adj}(A) = [C_{ij}]^T$$
  $$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

---

## Bagian 4: Vektor di Ruang Euclidean & Information Retrieval

### 4.1 Operasi Vektor di $\mathbb{R}^n$
- **Norma (Panjang Vektor Euclidean)**:
  $$\|u\| = \sqrt{u_1^2 + u_2^2 + \dots + u_n^2} = \sqrt{u \cdot u}$$
- **Hasil Kali Titik (Dot Product)**:
  $$u \cdot v = \sum_{i=1}^n u_i v_i = \|u\| \|v\| \cos \theta$$
- **Ortogonalitas**: Dua vektor $u$ dan $v$ saling tegak lurus jika dan hanya jika $u \cdot v = 0$.
- **Proyeksi Ortogonal $u$ pada $v$**:
  $$\text{proj}_v u = \frac{u \cdot v}{\|v\|^2} v$$

### 4.2 Aplikasi pada Information Retrieval (Sistem Temu Balik Informasi)
- **Representasi Ruang Vektor (Vector Space Model)**:
  Dokumen $D_j$ dan kueri pencarian $Q$ direpresentasikan sebagai vektor frekuensi kata / bobot TF-IDF:
  $$d_j = (w_{1j}, w_{2j}, \dots, w_{tj})^T, \quad q = (w_{1q}, w_{2q}, \dots, w_{tq})^T$$
- **Cosine Similarity (Kemiripan Kosinus)**:
  $$\text{sim}(q, d_j) = \cos \theta = \frac{q \cdot d_j}{\|q\| \|d_j\|} = \frac{\sum_{i=1}^t w_{iq} w_{ij}}{\sqrt{\sum_{i=1}^t w_{iq}^2} \sqrt{\sum_{i=1}^t w_{ij}^2}}$$
  Nilai berada pada rentang $[0, 1]$. Semakin mendekati 1, semakin relevan dokumen terhadap kueri pencarian.

---

## Bagian 5: Ruang Vektor Umum, Basis, dan Dimensi

### 5.1 Subruang (Subspace)
Himpunan bagian $W \subseteq V$ adalah subruang dari ruang vektor $V$ jika dan hanya jika:
1. $W$ tidak kosong (vektor nol $0 \in W$).
2. Tertutup terhadap penjumlahan: $\forall u, v \in W \implies u + v \in W$.
3. Tertutup terhadap perkalian skalar: $\forall u \in W, k \in \mathbb{R} \implies ku \in W$.

### 5.2 Kombinasi Linier, Rentang (Span), dan Kebebasan Linier
- **Kombinasi Linier**: $v = c_1 v_1 + c_2 v_2 + \dots + c_k v_k$.
- **Rentang (*Span*)**: $\text{span}(S)$ adalah himpunan semua kombinasi linier dari vektor-vektor dalam $S$.
- **Bebas Linier (*Linearly Independent*)**: Persamaan $c_1 v_1 + c_2 v_2 + \dots + c_k v_k = 0$ hanya memiliki solusi trivial $c_1 = c_2 = \dots = c_k = 0$. Jika ada skalar yang tidak nol, maka himpunan tersebut **bergantung linier** (*linearly dependent*).

### 5.3 Basis dan Dimensi
- $B = \{v_1, v_2, \dots, v_n\}$ adalah **basis** bagi $V$ jika:
  1. $B$ bebas linier.
  2. $B$ merentang $V$ ($\text{span}(B) = V$).
- **Dimensi** ($\dim(V)$) adalah banyaknya vektor dalam basis $V$.
- **Teorema Dimensi (Rank-Nullity Theorem)**:
  Untuk matriks $A$ berukuran $m \times n$:
  $$\text{rank}(A) + \text{nullity}(A) = n \quad (\text{jumlah kolom})$$

---

## Bagian 6: Nilai Eigen, Vektor Eigen, dan Diagonalisasi

### 6.1 Persamaan Karakteristik
Vektor tak nol $x$ adalah vektor eigen dari matriks persegi $A$ jika:
$$A x = \lambda x \iff (\lambda I - A) x = 0$$
Nilai skalar $\lambda$ diperoleh dari **persamaan karakteristik**:
$$\det(\lambda I - A) = 0$$
Ruang eigen untuk $\lambda$ adalah ruang nol dari matriks $(\lambda I - A)$, yaitu himpunan semua solusi $(\lambda I - A) x = 0$.

### 6.2 Diagonalisasi
- Matriks $A$ berukuran $n \times n$ dapat didiagonalisasi jika dan hanya jika $A$ memiliki $n$ vektor eigen yang bebas linier.
- Bentuk diagonalisasi:
  $$P^{-1} A P = D \iff A = P D P^{-1}$$
  di mana matriks $P = [v_1 \mid v_2 \mid \dots \mid v_n]$ kolom-kolomnya adalah vektor-vektor eigen dari $A$, dan $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$.
- Menghitung perpangkatan matriks besar dengan efisien:
  $$A^k = P D^k P^{-1}$$

---

## Bagian 7: Dekomposisi Matriks (SVD, LU, QR)

### 7.1 Singular Value Decomposition (SVD)
Setiap matriks real $A \in \mathbb{R}^{m \times n}$ dapat difaktorkan menjadi:
$$A = U \Sigma V^T$$
- $U \in \mathbb{R}^{m \times m}$: Matriks ortogonal yang kolom-kolomnya adalah *left singular vectors* (vektor eigen ortonormal dari $A A^T$).
- $V \in \mathbb{R}^{n \times n}$: Matriks ortogonal yang kolom-kolomnya adalah *right singular vectors* (vektor eigen ortonormal dari $A^T A$).
- $\Sigma \in \mathbb{R}^{m \times n}$: Matriks pseudo-diagonal dengan nilai-nilai singular $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$, di mana $\sigma_i = \sqrt{\lambda_i(A^T A)}$.
- **Aplikasi**: Kompresi citra (Trunkasi SVD berorde rendah / Low-rank Approximation Teorema Eckart-Young-Mirsky), reduksi dimensi (PCA), *latent semantic analysis*.

### 7.2 Dekomposisi LU
Memfaktorkan matriks persegi $A$ menjadi:
$$A = L U$$
- $L$ (*Lower triangular*): Matriks segitiga bawah (elemen diagonal bernilai 1 pada dekomposisi Doolittle).
- $U$ (*Upper triangular*): Matriks segitiga atas (hasil eliminasi Gauss).
- Menyelesaikan $Ax = b$ menjadi 2 tahap cepat tanpa eliminasi ulang:
  1. $L y = b$ (substitusi maju / *forward substitution*)
  2. $U x = y$ (substitusi balik / *back substitution*)

### 7.3 Dekomposisi QR
Memfaktorkan matriks $A \in \mathbb{R}^{m \times n}$ dengan kolom-kolom bebas linier menjadi:
$$A = Q R$$
- $Q \in \mathbb{R}^{m \times n}$: Matriks dengan kolom-kolom yang ortonormal ($Q^T Q = I$), diperoleh menggunakan proses **Gram-Schmidt**.
- $R \in \mathbb{R}^{n \times n}$: Matriks segitiga atas yang dapat dibalik.
- **Aplikasi**: Solusi masalah kuadrat terkecil (*least squares problem*), algoritma iterasi QR untuk mencari seluruh nilai eigen secara numerik.

---

## Bagian 8: Penerapan Praktis & Persiapan Tugas Besar 1

Tugas Besar 1 (Tubes 1) menekankan implementasi komputasi numerik aljabar linier dalam pemrograman (Java / GUI / CLI):

### 8.1 Menu Wajib Tubes 1
1. **Solusi Sistem Persamaan Linier**:
   - Metode Eliminasi Gauss
   - Metode Eliminasi Gauss-Jordan
   - Metode Matriks Balikan ($x = A^{-1} b$)
   - Kaidah Cramer
2. **Determinan**:
   - Reduksi Baris (Operasi Baris Elementer)
   - Ekspansi Kofaktor
3. **Invers Matriks**:
   - Reduksi Baris Gauss-Jordan $[A \mid I] \to [I \mid A^{-1}]$
   - Matriks Adjoin
4. **Interpolasi Polinomial**:
   - Membentuk matriks Vandermonde dari pasangan titik $(x_i, y_i)$:
     $$p(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n$$
5. **Natural Cubic Spline Interpolation**:
   - Mengonstruksi potongan kurva polinomial kubik $S_i(x) = a_i + b_i(x-x_i) + c_i(x-x_i)^2 + d_i(x-x_i)^3$ dengan kontinuitas turunan pertama dan kedua serta syarat natural $S''(x_0) = S''(x_n) = 0$.
6. **Regresi Spline**:
   - Pendekatan kurva fleksibel berbasis piecewise polynomial dengan penempatan knot untuk fitting data ber-noise.

---

*Disusun secara otomatis dari bahan kuliah IF2123 Aljabar Linier dan Geometri STEI ITB.*
