"""
================================================================================
ANIMASI MANIM: OPERASI BARIS ELEMENTER & MATRIKS ESELON (UNU KALBAR)
Dosen     : Aditya Pratama
Topik     : Algeo 02
================================================================================
"""

from manim import *

class AnimasiMatriksEselon(Scene):
    def construct(self):
        # 1. Header UNU Kalbar
        header = Text("Algeo 02: Pembentukan Matriks Eselon Baris (REF)", font_size=26, color=BLUE_B).to_edge(UP)
        dosen = Text("UNU Kalbar • Dosen: Aditya Pratama", font_size=16, color=GRAY_B).next_to(header, DOWN, buff=0.1)
        self.play(FadeIn(header), FadeIn(dosen))
        self.wait(1)

        # 2. Matriks Awal
        mat_text_1 = Text("[  2.0    4.0   -2.0  ]\n[  1.0    3.0    4.0  ]\n[  5.0    2.0   -1.0  ]", font_size=24, font="Consolas").shift(UP * 0.5)
        label_1 = Text("Matriks Awal: Elemen pertama baris 1 adalah 2 (Bukan 1 Utama)", font_size=16, color=RED_C).next_to(mat_text_1, DOWN, buff=0.4)

        self.play(FadeIn(mat_text_1), Write(label_1))
        self.wait(2)

        # 3. Operasi R1 <- R1 / 2
        op1 = Text("OBE: Baris 1 dibagi 2 (R1 <- R1 / 2)", font_size=20, color=YELLOW).to_edge(LEFT).shift(UP * 0.5)
        mat_text_2 = Text("[  1.0    2.0   -1.0  ]\n[  1.0    3.0    4.0  ]\n[  5.0    2.0   -1.0  ]", font_size=24, font="Consolas").shift(UP * 0.5)
        label_2 = Text("1 Utama Terbentuk di Baris 1 Kolom 1 (Leading 1)", font_size=16, color=GREEN_C).next_to(mat_text_2, DOWN, buff=0.4)

        box_pivot = Rectangle(width=0.8, height=0.6, color=GREEN).move_to(mat_text_2.get_corner(UL)).shift(RIGHT * 0.5 + DOWN * 0.35)

        self.play(FadeOut(label_1), Write(op1), Transform(mat_text_1, mat_text_2), run_time=1.5)
        self.play(Create(box_pivot), FadeIn(label_2))
        self.wait(2)

        # 4. Operasi Eliminasi di bawah 1 Utama
        self.play(FadeOut(op1), FadeOut(box_pivot), FadeOut(label_2))

        op2 = Text("OBE: Nol-kan angka di bawah 1 utama (R2 <- R2 - R1, R3 <- R3 - 5*R1)", font_size=18, color=YELLOW).to_edge(LEFT).shift(UP * 0.5)
        mat_ref = Text("[  1.0    2.0   -1.0  ]\n[  0.0    1.0    5.0  ]\n[  0.0    0.0    1.0  ]", font_size=24, font="Consolas").shift(UP * 0.5)
        label_ref = Text("Status: Matriks Eselon Baris (REF) Sah! (Pola Tangga Terbentuk)", font_size=16, color=GREEN_B).next_to(mat_ref, DOWN, buff=0.4)

        self.play(Write(op2), Transform(mat_text_1, mat_ref), run_time=2)
        self.play(FadeIn(label_ref))
        self.wait(2)

        # 5. Gauss-Jordan ke RREF
        self.play(FadeOut(op2), FadeOut(label_ref))

        op3 = Text("Gauss-Jordan: Nol-kan entri di ATAS 1 utama", font_size=18, color=TEAL).to_edge(LEFT).shift(UP * 0.5)
        mat_rref = Text("[  1.0    0.0    0.0  ]\n[  0.0    1.0    0.0  ]\n[  0.0    0.0    1.0  ]", font_size=26, font="Consolas", color=BLUE_B).shift(UP * 0.5)
        label_rref = Text("Status: Eselon Baris Tereduksi (RREF) = Matriks Identitas I3", font_size=16, color=YELLOW_B).next_to(mat_rref, DOWN, buff=0.4)

        self.play(Write(op3), Transform(mat_text_1, mat_rref), run_time=2)
        self.play(FadeIn(label_rref))
        self.wait(2)
