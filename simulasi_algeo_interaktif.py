"""
================================================================================
SIMULASI & VISUALISASI INTERAKTIF ALJABAR LINIER (ALGEO 00 & ALGEO 02)
Universitas Nahdlatul Ulama Kalimantan Barat (UNU Kalbar)
Dosen Pengampu : Aditya Pratama
Referensi     : Rinaldi Munir (STEI ITB) & Howard Anton
================================================================================
Fitur Utama:
1. Tab 1 (Algeo 00): Animasi Interaktif Transformasi Geometri 2D & Matriks
   - Visualisasi Grid Koordinat, Vektor Basis i-hat dan j-hat
   - Animasi Rotasi, Skala (Scaling), Shear, Refleksi
   - Interpolasi perpindahan titik halus (smooth interpolation)
2. Tab 2 (Algeo 02): Simulator Animasi Operasi Baris Elementer (OBE)
   - Step-by-step eliminasi Gauss (REF) dan Gauss-Jordan (RREF)
   - Penjelasan detail setiap langkah (Pivot / 1 Utama, Baris Eliminasi)
   - Pengenalan 3 Sifat REF dan Sifat ke-4 RREF
3. Tab 3 (Algeo 00): Simulasi Cosine Similarity (Information Retrieval)
   - Visualisasi sudut antar vektor dokumen dan vektor kueri
================================================================================
"""

import sys
import os
import math
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox

# Integrasi Matplotlib ke Tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

# Warna tema modern
COLOR_BG = "#0f172a"        # Slate 900
COLOR_CARD = "#1e293b"      # Slate 800
COLOR_BORDER = "#334155"    # Slate 700
COLOR_TEXT = "#f8fafc"      # Slate 50
COLOR_MUTED = "#94a3b8"     # Slate 400
COLOR_PRIMARY = "#38bdf8"   # Sky 400
COLOR_ACCENT = "#818cf8"    # Indigo 400
COLOR_SUCCESS = "#34d399"   # Emerald 400
COLOR_WARN = "#fbbf24"      # Amber 400

class AlgeoSimulatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulasi Aljabar Linier & Geometri - UNU Kalbar (Aditya Pratama)")
        self.geometry("1100x720")
        self.minsize(980, 640)
        self.configure(bg=COLOR_BG)

        # Style TTK
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background=COLOR_BG, foreground=COLOR_TEXT, font=("Segoe UI", 10))
        self.style.configure("TNotebook", background=COLOR_BG, borderwidth=0)
        self.style.configure("TNotebook.Tab", background=COLOR_CARD, foreground=COLOR_TEXT,
                               padding=[16, 8], font=("Segoe UI", 10, "bold"))
        self.style.map("TNotebook.Tab",
                       background=[("selected", COLOR_PRIMARY)],
                       foreground=[("selected", "#0f172a")])

        # Header Info Dosen & Kampus
        self._build_header()

        # Notebook (Tabbed Interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=16, pady=10)

        # Inisialisasi Tab
        self.tab_transform = ttk.Frame(self.notebook)
        self.tab_eselon = ttk.Frame(self.notebook)
        self.tab_ir = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_transform, text="Algeo 00: Transformasi Geometri 2D")
        self.notebook.add(self.tab_eselon, text="Algeo 02: Eliminasi Matriks Eselon (OBE)")
        self.notebook.add(self.tab_ir, text="Algeo 00: Cosine Similarity (IR)")

        self._init_tab_transform()
        self._init_tab_eselon()
        self._init_tab_ir()

    def _build_header(self):
        header_frame = tk.Frame(self, bg=COLOR_CARD, height=75, bd=1, relief=tk.SOLID)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        # Muat Logo UNU Kalbar jika ada
        logo_path = os.path.join(os.path.dirname(__file__), "logo_unukalbar.png")
        self.logo_img = None
        if os.path.exists(logo_path):
            try:
                from PIL import Image, ImageTk
                img = Image.open(logo_path)
                img = img.resize((48, 56), Image.Resampling.LANCZOS)
                self.logo_img = ImageTk.PhotoImage(img)
                lbl_logo = tk.Label(header_frame, image=self.logo_img, bg=COLOR_CARD)
                lbl_logo.pack(side=tk.LEFT, padx=(16, 12), pady=8)
            except Exception as e:
                pass

        text_frame = tk.Frame(header_frame, bg=COLOR_CARD)
        text_frame.pack(side=tk.LEFT, fill=tk.Y, pady=6)

        title_label = tk.Label(
            text_frame,
            text="UNIVERSITAS NAHDLATUL ULAMA KALIMANTAN BARAT (UNU KALBAR)",
            bg=COLOR_CARD, fg=COLOR_PRIMARY,
            font=("Segoe UI", 11, "bold")
        )
        title_label.pack(anchor="w")

        sub_label = tk.Label(
            text_frame,
            text="Media Simulasi Perkuliahan Matematika 2 / Aljabar Linier & Geometri • Dosen: Aditya Pratama",
            bg=COLOR_CARD, fg=COLOR_MUTED,
            font=("Segoe UI", 9)
        )
        sub_label.pack(anchor="w", pady=(2, 0))

    # =========================================================================
    # TAB 1: ANIMASI TRANSFORMASI 2D (ALGEO 00)
    # =========================================================================
    def _init_tab_transform(self):
        left_panel = tk.Frame(self.tab_transform, bg=COLOR_CARD, width=320, padx=15, pady=15)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 5), pady=10)

        tk.Label(left_panel, text="Kontrol Matriks Transformasi", bg=COLOR_CARD, fg=COLOR_PRIMARY,
                 font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 10))

        # Preset tombol cepat
        tk.Label(left_panel, text="Pilih Preset Transformasi:", bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w")
        btn_frame = tk.Frame(left_panel, bg=COLOR_CARD)
        btn_frame.pack(fill=tk.X, pady=6)

        presets = [
            ("Identitas", [[1, 0], [0, 1]]),
            ("Rotasi 45°", [[math.cos(math.pi/4), -math.sin(math.pi/4)],
                            [math.sin(math.pi/4), math.cos(math.pi/4)]]),
            ("Rotasi 90°", [[0, -1], [1, 0]]),
            ("Skala 1.5x", [[1.5, 0], [0, 1.5]]),
            ("Shear X", [[1, 1], [0, 1]]),
            ("Refleksi Y", [[-1, 0], [0, 1]])
        ]

        for i, (name, m) in enumerate(presets):
            b = tk.Button(btn_frame, text=name, bg="#334155", fg=COLOR_TEXT, activebackground=COLOR_PRIMARY,
                          activeforeground="#0f172a", font=("Segoe UI", 8),
                          command=lambda mat=m: self._apply_matrix_preset(mat))
            b.grid(row=i//2, column=i%2, padx=3, pady=3, sticky="ew")
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)

        # Input Manual Matriks
        tk.Label(left_panel, text="\nMatriks Transformasi T = [a b; c d]:", bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w")
        m_frame = tk.Frame(left_panel, bg=COLOR_CARD)
        m_frame.pack(fill=tk.X, pady=4)

        self.entry_a = tk.Entry(m_frame, width=6, justify="center", font=("Consolas", 10))
        self.entry_b = tk.Entry(m_frame, width=6, justify="center", font=("Consolas", 10))
        self.entry_c = tk.Entry(m_frame, width=6, justify="center", font=("Consolas", 10))
        self.entry_d = tk.Entry(m_frame, width=6, justify="center", font=("Consolas", 10))

        self.entry_a.insert(0, "1.0")
        self.entry_b.insert(0, "0.0")
        self.entry_c.insert(0, "0.0")
        self.entry_d.insert(0, "1.0")

        self.entry_a.grid(row=0, column=0, padx=4, pady=3)
        self.entry_b.grid(row=0, column=1, padx=4, pady=3)
        self.entry_c.grid(row=1, column=0, padx=4, pady=3)
        self.entry_d.grid(row=1, column=1, padx=4, pady=3)

        btn_run = tk.Button(left_panel, text="▶ Jalankan Animasi Transformasi", bg=COLOR_PRIMARY, fg="#0f172a",
                            font=("Segoe UI", 10, "bold"), pady=6, cursor="hand2",
                            command=self._start_transform_animation)
        btn_run.pack(fill=tk.X, pady=(15, 8))

        btn_reset = tk.Button(left_panel, text="↺ Reset Grid", bg="#475569", fg=COLOR_TEXT,
                              font=("Segoe UI", 9), command=self._reset_transform)
        btn_reset.pack(fill=tk.X)

        # Penjelasan Teori Singkat
        tk.Label(left_panel, text="\nKaitan Algeo 00:", bg=COLOR_CARD, fg=COLOR_WARN,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        info_txt = (
            "• Setiap kolom matriks T adalah posisi baru dari vektor basis:\n"
            "  - Kolom 1 = Posisi baru i-hat (1, 0)\n"
            "  - Kolom 2 = Posisi baru j-hat (0, 1)\n"
            "• Menjadi dasar rendering di OpenGL, GPU, & game engine 3D!"
        )
        tk.Label(left_panel, text=info_txt, bg=COLOR_CARD, fg=COLOR_MUTED,
                 font=("Segoe UI", 8), justify="left", wraplength=280).pack(anchor="w")

        # Kanvas Matplotlib
        right_panel = tk.Frame(self.tab_transform, bg=COLOR_BG)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.fig_trans = Figure(figsize=(6, 5), facecolor=COLOR_CARD)
        self.ax_trans = self.fig_trans.add_subplot(111)
        self._setup_trans_axis()

        self.canvas_trans = FigureCanvasTkAgg(self.fig_trans, master=right_panel)
        self.canvas_trans.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.anim_trans = None
        self.curr_matrix = np.eye(2)
        self.target_matrix = np.eye(2)
        self._draw_trans_frame(self.curr_matrix)

    def _setup_trans_axis(self):
        self.ax_trans.clear()
        self.ax_trans.set_facecolor("#0b1120")
        self.ax_trans.set_xlim(-3.5, 3.5)
        self.ax_trans.set_ylim(-3.5, 3.5)
        self.ax_trans.set_aspect("equal")
        self.ax_trans.grid(True, color="#1e293b", linestyle="--", alpha=0.7)
        self.ax_trans.axhline(0, color="#475569", linewidth=1.2)
        self.ax_trans.axvline(0, color="#475569", linewidth=1.2)
        self.ax_trans.tick_params(colors=COLOR_MUTED, labelsize=8)

    def _apply_matrix_preset(self, mat):
        self.entry_a.delete(0, tk.END); self.entry_a.insert(0, f"{mat[0][0]:.2f}")
        self.entry_b.delete(0, tk.END); self.entry_b.insert(0, f"{mat[0][1]:.2f}")
        self.entry_c.delete(0, tk.END); self.entry_c.insert(0, f"{mat[1][0]:.2f}")
        self.entry_d.delete(0, tk.END); self.entry_d.insert(0, f"{mat[1][1]:.2f}")
        self._start_transform_animation()

    def _start_transform_animation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            d = float(self.entry_d.get())
            self.target_matrix = np.array([[a, b], [c, d]])
        except ValueError:
            messagebox.showerror("Error", "Entri matriks harus berupa angka valid.")
            return

        if self.anim_trans is not None and self.anim_trans.event_source is not None:
            self.anim_trans.event_source.stop()

        start_mat = self.curr_matrix.copy()
        frames = 30

        def update(frame):
            alpha = frame / frames
            # Smooth ease-in-out
            s = 3 * alpha**2 - 2 * alpha**3
            interp_mat = (1 - s) * start_mat + s * self.target_matrix
            self._draw_trans_frame(interp_mat)
            if frame == frames:
                self.curr_matrix = self.target_matrix.copy()

        self.anim_trans = animation.FuncAnimation(
            self.fig_trans, update, frames=frames + 1, interval=25, repeat=False
        )
        self.canvas_trans.draw()

    def _reset_transform(self):
        self._apply_matrix_preset([[1, 0], [0, 1]])

    def _draw_trans_frame(self, mat):
        self._setup_trans_axis()

        # Grid garis halus bertransformasi
        grid_range = np.linspace(-3, 3, 7)
        for g in grid_range:
            # Garis vertikal & horizontal awal
            pts_v = np.array([[g, g], [-3.5, 3.5]])
            pts_h = np.array([[-3.5, 3.5], [g, g]])
            t_v = mat @ pts_v
            t_h = mat @ pts_h
            self.ax_trans.plot(t_v[0], t_v[1], color="#334155", linewidth=0.8, alpha=0.5)
            self.ax_trans.plot(t_h[0], t_h[1], color="#334155", linewidth=0.8, alpha=0.5)

        # Poligon Bentuk Objek Kotak Unit
        square = np.array([
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0]
        ])
        t_square = mat @ square
        self.ax_trans.fill(t_square[0], t_square[1], color=COLOR_PRIMARY, alpha=0.25)
        self.ax_trans.plot(t_square[0], t_square[1], color=COLOR_PRIMARY, linewidth=2, label="Objek Poligon")

        # Vektor Basis i-hat dan j-hat
        ihat = mat @ np.array([1, 0])
        jhat = mat @ np.array([0, 1])

        self.ax_trans.quiver(0, 0, ihat[0], ihat[1], angles='xy', scale_units='xy', scale=1,
                             color=COLOR_SUCCESS, width=0.015, label=f"i-hat ({ihat[0]:.1f}, {ihat[1]:.1f})")
        self.ax_trans.quiver(0, 0, jhat[0], jhat[1], angles='xy', scale_units='xy', scale=1,
                             color=COLOR_ACCENT, width=0.015, label=f"j-hat ({jhat[0]:.1f}, {jhat[1]:.1f})")

        det_val = np.linalg.det(mat)
        self.ax_trans.set_title(f"Transformasi Matriks T • Det(T) = {det_val:.2f}",
                                color=COLOR_TEXT, fontsize=10, pad=8)
        self.ax_trans.legend(loc="upper left", facecolor="#1e293b", edgecolor="#334155",
                             fontsize=8, labelcolor=COLOR_TEXT)
        self.canvas_trans.draw_idle()

    # =========================================================================
    # TAB 2: SIMULATOR LANGKAH MATRIKS ESELON / OBE (ALGEO 02)
    # =========================================================================
    def _init_tab_eselon(self):
        panel = tk.Frame(self.tab_eselon, bg=COLOR_BG)
        panel.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Sisi Kontrol Atas
        top_ctrl = tk.Frame(panel, bg=COLOR_CARD, padx=15, pady=12, bd=1, relief=tk.SOLID)
        top_ctrl.pack(fill=tk.X, pady=(0, 10))

        tk.Label(top_ctrl, text="Eksplorasi Langkah Eliminasi Gauss (REF) & Gauss-Jordan (RREF)",
                 bg=COLOR_CARD, fg=COLOR_PRIMARY, font=("Segoe UI", 11, "bold")).pack(anchor="w")

        btn_row = tk.Frame(top_ctrl, bg=COLOR_CARD)
        btn_row.pack(fill=tk.X, pady=8)

        presets = [
            ("Contoh 1: 3x4 Standar", [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]),
            ("Contoh 2: Butuh Tukar Baris", [[0, 2, 4, 12], [2, 4, 2, 10], [1, 1, 1, 4]]),
            ("Contoh 3: Solusi Banyak", [[1, 2, -1, 4], [2, 4, -2, 8], [1, 3, 2, 5]]),
            ("Contoh 4: Matriks 3x3", [[1, 2, 3], [2, 5, 3], [1, 0, 8]])
        ]

        for name, mat in presets:
            b = tk.Button(btn_row, text=name, bg="#334155", fg=COLOR_TEXT, font=("Segoe UI", 8),
                          command=lambda m=mat: self._load_eselon_matrix(m))
            b.pack(side=tk.LEFT, padx=4)

        # Kontrol Langkah
        step_ctrl = tk.Frame(top_ctrl, bg=COLOR_CARD)
        step_ctrl.pack(fill=tk.X, pady=4)

        self.btn_prev_step = tk.Button(step_ctrl, text="◀ Langkah Sebelumnya", bg="#475569", fg=COLOR_TEXT,
                                       font=("Segoe UI", 9), command=self._prev_eselon_step)
        self.btn_prev_step.pack(side=tk.LEFT, padx=(0, 6))

        self.btn_next_step = tk.Button(step_ctrl, text="Langkah Berikutnya ▶", bg=COLOR_PRIMARY, fg="#0f172a",
                                       font=("Segoe UI", 9, "bold"), command=self._next_eselon_step)
        self.btn_next_step.pack(side=tk.LEFT, padx=6)

        self.lbl_step_info = tk.Label(step_ctrl, text="Langkah: 0 / 0", bg=COLOR_CARD, fg=COLOR_WARN,
                                      font=("Segoe UI", 9, "bold"))
        self.lbl_step_info.pack(side=tk.LEFT, padx=12)

        # Tampilan Tengah: Matriks & Deskripsi
        mid_frame = tk.Frame(panel, bg=COLOR_BG)
        mid_frame.pack(fill=tk.BOTH, expand=True)

        # Kiri: Matrix Display
        self.matrix_display_frame = tk.Frame(mid_frame, bg=COLOR_CARD, padx=20, pady=20, bd=1, relief=tk.SOLID)
        self.matrix_display_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

        tk.Label(self.matrix_display_frame, text="Kondisi Matriks Saat Ini:", bg=COLOR_CARD, fg=COLOR_PRIMARY,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 10))

        self.lbl_matrix_text = tk.Label(self.matrix_display_frame, text="", bg="#0b1120", fg=COLOR_TEXT,
                                        font=("Consolas", 14), justify="center", padx=25, pady=20,
                                        bd=1, relief=tk.SOLID)
        self.lbl_matrix_text.pack(fill=tk.BOTH, expand=True, pady=6)

        self.lbl_status_eselon = tk.Label(self.matrix_display_frame, text="Status: Mengevaluasi...",
                                          bg=COLOR_CARD, fg=COLOR_SUCCESS, font=("Segoe UI", 10, "bold"))
        self.lbl_status_eselon.pack(anchor="w", pady=(8, 0))

        # Kanan: Log Penjelasan Langkah OBE
        log_frame = tk.Frame(mid_frame, bg=COLOR_CARD, width=380, padx=15, pady=15, bd=1, relief=tk.SOLID)
        log_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(8, 0))

        tk.Label(log_frame, text="Log Penjelasan Operasi Baris Elementer (OBE):", bg=COLOR_CARD, fg=COLOR_PRIMARY,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 8))

        self.txt_eselon_log = tk.Text(log_frame, bg="#0b1120", fg=COLOR_TEXT, font=("Segoe UI", 9),
                                      width=40, height=18, bd=0, padx=10, pady=10, wrap=tk.WORD)
        self.txt_eselon_log.pack(fill=tk.BOTH, expand=True)

        # Data solver langkah
        self.eselon_steps = []
        self.current_eselon_idx = 0
        self._load_eselon_matrix([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])

    def _load_eselon_matrix(self, mat_raw):
        mat = np.array(mat_raw, dtype=float)
        self.eselon_steps = self._compute_gauss_jordan_steps(mat)
        self.current_eselon_idx = 0
        self._render_eselon_step()

    def _compute_gauss_jordan_steps(self, mat_orig):
        steps = []
        M = mat_orig.copy()
        rows, cols = M.shape

        steps.append({
            "mat": M.copy(),
            "desc": "Kondisi matriks awal sebelum Operasi Baris Elementer (OBE) dimulai.",
            "op": "Inisialisasi"
        })

        pivot_row = 0
        for c in range(cols - 1 if cols > rows else cols):
            if pivot_row >= rows:
                break

            # 1. Cari baris dengan elemen mutlak terbesar pada kolom c (partial pivoting)
            max_r = pivot_row + np.argmax(np.abs(M[pivot_row:, c]))
            if np.isclose(M[max_r, c], 0.0):
                continue

            # Tukar baris jika diperlukan (Sifat 3 & stabilitas numerik)
            if max_r != pivot_row:
                M[[pivot_row, max_r]] = M[[max_r, pivot_row]]
                steps.append({
                    "mat": M.copy(),
                    "desc": f"Tukar Baris R{pivot_row+1} ↔ R{max_r+1} agar elemen bukan-nol berada di posisi pivot.",
                    "op": f"R{pivot_row+1} ↔ R{max_r+1}"
                })

            # 2. Jadikan elemen pivot menjadi 1 Utama (Sifat 1 REF)
            pivot_val = M[pivot_row, c]
            if not np.isclose(pivot_val, 1.0):
                M[pivot_row] = M[pivot_row] / pivot_val
                steps.append({
                    "mat": M.copy(),
                    "desc": f"Bagi Baris R{pivot_row+1} dengan {pivot_val:.2f} untuk menciptakan 1 UTAMA (Leading 1).",
                    "op": f"R{pivot_row+1} ← R{pivot_row+1} / ({pivot_val:.2f})"
                })

            # 3. Nol-kan elemen di bawah 1 utama (Sifat REF)
            for r in range(pivot_row + 1, rows):
                factor = M[r, c]
                if not np.isclose(factor, 0.0):
                    M[r] = M[r] - factor * M[pivot_row]
                    steps.append({
                        "mat": M.copy(),
                        "desc": f"Nol-kan entri di bawah 1 utama: Baris R{r+1} ← R{r+1} - ({factor:.2f}) * R{pivot_row+1}.",
                        "op": f"R{r+1} ← R{r+1} - ({factor:.2f})R{pivot_row+1}"
                    })

            pivot_row += 1

        steps.append({
            "mat": M.copy(),
            "desc": "Tahap Eliminasi Gauss Selesai: Matriks berada dalam bentuk Eselon Baris (REF).",
            "op": "REF Tercapai"
        })

        # 4. Tahap Gauss-Jordan (Nol-kan entri di ATAS 1 utama untuk mencapai RREF)
        for r in range(rows - 1, -1, -1):
            leading_cols = np.where(np.abs(M[r]) > 1e-6)[0]
            if len(leading_cols) == 0:
                continue
            lead_c = leading_cols[0]
            if lead_c >= cols:
                continue

            for above_r in range(r - 1, -1, -1):
                factor = M[above_r, lead_c]
                if not np.isclose(factor, 0.0):
                    M[above_r] = M[above_r] - factor * M[r]
                    steps.append({
                        "mat": M.copy(),
                        "desc": f"Gauss-Jordan: Nol-kan entri di ATAS 1 utama: R{above_r+1} ← R{above_r+1} - ({factor:.2f}) * R{r+1}.",
                        "op": f"R{above_r+1} ← R{above_r+1} - ({factor:.2f})R{r+1}"
                    })

        steps.append({
            "mat": M.copy(),
            "desc": "Tahap Gauss-Jordan Selesai: Matriks berada dalam bentuk Eselon Baris Tereduksi (RREF).",
            "op": "RREF Tercapai"
        })

        return steps

    def _render_eselon_step(self):
        if not self.eselon_steps:
            return

        step = self.eselon_steps[self.current_eselon_idx]
        M = step["mat"]
        total = len(self.eselon_steps)

        self.lbl_step_info.config(text=f"Langkah: {self.current_eselon_idx + 1} / {total}  [{step['op']}]")

        # Format visual matriks string
        mat_str = ""
        rows, cols = M.shape
        for r in range(rows):
            line = "[  "
            for c in range(cols):
                val = M[r, c]
                if np.isclose(val, 0.0):
                    val = 0.0
                line += f"{val:7.2f}  "
            line += "]\n"
            mat_str += line

        self.lbl_matrix_text.config(text=mat_str)

        # Status Eselon
        if self.current_eselon_idx == total - 1:
            self.lbl_status_eselon.config(text="Status: Eselon Baris Tereduksi (RREF) Terpenuhi", fg=COLOR_SUCCESS)
        elif self.current_eselon_idx >= total - 3:
            self.lbl_status_eselon.config(text="Status: Matriks Eselon Baris (REF) Terpenuhi", fg=COLOR_PRIMARY)
        else:
            self.lbl_status_eselon.config(text="Status: Eliminasi OBE Berjalan...", fg=COLOR_WARN)

        # Log deskripsi
        self.txt_eselon_log.delete("1.0", tk.END)
        for i in range(self.current_eselon_idx + 1):
            s = self.eselon_steps[i]
            prefix = "▶ " if i == self.current_eselon_idx else "  "
            self.txt_eselon_log.insert(tk.END, f"{prefix}Langkah {i+1} ({s['op']}):\n{s['desc']}\n\n")
        self.txt_eselon_log.see(tk.END)

        self.btn_prev_step.config(state=tk.NORMAL if self.current_eselon_idx > 0 else tk.DISABLED)
        self.btn_next_step.config(state=tk.NORMAL if self.current_eselon_idx < total - 1 else tk.DISABLED)

    def _next_eselon_step(self):
        if self.current_eselon_idx < len(self.eselon_steps) - 1:
            self.current_eselon_idx += 1
            self._render_eselon_step()

    def _prev_eselon_step(self):
        if self.current_eselon_idx > 0:
            self.current_eselon_idx -= 1
            self._render_eselon_step()

    # =========================================================================
    # TAB 3: SIMULASI COSINE SIMILARITY / INFORMATION RETRIEVAL (ALGEO 00)
    # =========================================================================
    def _init_tab_ir(self):
        panel = tk.Frame(self.tab_ir, bg=COLOR_BG)
        panel.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        left = tk.Frame(panel, bg=COLOR_CARD, width=340, padx=15, pady=15, bd=1, relief=tk.SOLID)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        tk.Label(left, text="Aplikasi Algeo: Vector Space Model & Mesin Pencari",
                 bg=COLOR_CARD, fg=COLOR_PRIMARY, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 10))

        tk.Label(left, text="Kueri Pencarian Q (x, y):", bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w")
        q_frame = tk.Frame(left, bg=COLOR_CARD)
        q_frame.pack(fill=tk.X, pady=4)
        self.eq_x = tk.Scale(q_frame, from_=0, to=5, resolution=0.2, orient=tk.HORIZONTAL,
                             bg=COLOR_CARD, fg=COLOR_TEXT, label="Bobot Kata 1 (Aljabar)",
                             command=lambda v: self._update_ir_plot())
        self.eq_x.set(3.0)
        self.eq_x.pack(fill=tk.X)

        self.eq_y = tk.Scale(q_frame, from_=0, to=5, resolution=0.2, orient=tk.HORIZONTAL,
                             bg=COLOR_CARD, fg=COLOR_TEXT, label="Bobot Kata 2 (Geometri)",
                             command=lambda v: self._update_ir_plot())
        self.eq_y.set(4.0)
        self.eq_y.pack(fill=tk.X)

        tk.Label(left, text="\nDokumen Terindeks (Database):", bg=COLOR_CARD, fg=COLOR_TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w")
        doc_info = (
            "• Dokumen A: D1 = (4, 4) [Artikel Algeo]\n"
            "• Dokumen B: D2 = (1, 5) [Artikel Geometri]\n"
            "• Dokumen C: D3 = (5, 1) [Artikel Aljabar Murni]"
        )
        tk.Label(left, text=doc_info, bg=COLOR_CARD, fg=COLOR_MUTED, justify="left", font=("Segoe UI", 9)).pack(anchor="w", pady=4)

        self.lbl_ir_ranking = tk.Label(left, text="Hasil Peringkat:", bg="#0b1120", fg=COLOR_SUCCESS,
                                       font=("Consolas", 10), justify="left", padx=10, pady=10,
                                       bd=1, relief=tk.SOLID)
        self.lbl_ir_ranking.pack(fill=tk.X, pady=(15, 0))

        # Right: Matplotlib Plot
        right = tk.Frame(panel, bg=COLOR_BG)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig_ir = Figure(figsize=(5, 5), facecolor=COLOR_CARD)
        self.ax_ir = self.fig_ir.add_subplot(111)
        self.canvas_ir = FigureCanvasTkAgg(self.fig_ir, master=right)
        self.canvas_ir.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self._update_ir_plot()

    def _update_ir_plot(self):
        self.ax_ir.clear()
        self.ax_ir.set_facecolor("#0b1120")
        self.ax_ir.set_xlim(0, 6)
        self.ax_ir.set_ylim(0, 6)
        self.ax_ir.grid(True, color="#1e293b", linestyle="--", alpha=0.7)
        self.ax_ir.set_xlabel("Frekuensi Kata: 'Aljabar'", color=COLOR_MUTED, fontsize=9)
        self.ax_ir.set_ylabel("Frekuensi Kata: 'Geometri'", color=COLOR_MUTED, fontsize=9)
        self.ax_ir.tick_params(colors=COLOR_MUTED, labelsize=8)

        qx = self.eq_x.get()
        qy = self.eq_y.get()
        q = np.array([qx, qy])

        docs = {
            "Dokumen A (4, 4)": np.array([4.0, 4.0]),
            "Dokumen B (1, 5)": np.array([1.0, 5.0]),
            "Dokumen C (5, 1)": np.array([5.0, 1.0])
        }

        # Plot Kueri
        self.ax_ir.quiver(0, 0, q[0], q[1], angles='xy', scale_units='xy', scale=1,
                          color=COLOR_PRIMARY, width=0.015, label=f"Kueri Q ({qx:.1f}, {qy:.1f})")

        colors = ["#a78bfa", "#f59e0b", "#ec4899"]
        scores = []

        norm_q = np.linalg.norm(q)
        for i, (name, d) in enumerate(docs.items()):
            c = colors[i]
            self.ax_ir.quiver(0, 0, d[0], d[1], angles='xy', scale_units='xy', scale=1,
                              color=c, width=0.012, label=name)
            # Hitung Cosine Similarity
            norm_d = np.linalg.norm(d)
            if norm_q > 0 and norm_d > 0:
                sim = np.dot(q, d) / (norm_q * norm_d)
            else:
                sim = 0.0
            scores.append((name, sim))

        scores.sort(key=lambda x: x[1], reverse=True)

        rank_txt = "HASIL PERINGKAT KEMIRIPAN (COSINE SIMILARITY):\n"
        rank_txt += "="*40 + "\n"
        for rank, (name, s) in enumerate(scores):
            rank_txt += f"#{rank+1} {name:16}: Cos θ = {s:.4f} ({s*100:.1f}%)\n"

        self.lbl_ir_ranking.config(text=rank_txt)

        self.ax_ir.set_title("Visualisasi Sudut Vektor Dokumen vs Kueri", color=COLOR_TEXT, fontsize=10, pad=8)
        self.ax_ir.legend(loc="upper right", facecolor="#1e293b", edgecolor="#334155",
                          fontsize=8, labelcolor=COLOR_TEXT)
        self.canvas_ir.draw_idle()


if __name__ == "__main__":
    app = AlgeoSimulatorApp()
    app.mainloop()
