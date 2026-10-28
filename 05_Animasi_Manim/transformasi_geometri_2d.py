"""
================================================================================
ANIMASI MANIM: TRANSFORMASI LINIER 2D (UNU KALBAR)
Dosen     : Aditya Pratama
Topik     : Algeo 00 & Algeo 18
================================================================================
"""

from manim import *

class AnimasiTransformasi2D(Scene):
    def construct(self):
        # 1. Judul & Dosen
        title = Text("Transformasi Matriks 2D — UNU Kalbar", font_size=28, color=BLUE_B).to_edge(UP)
        sub = Text("Dosen: Aditya Pratama • Aljabar Linier & Geometri", font_size=16, color=GRAY_B).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(sub))
        self.wait(1)

        # 2. Grid Koordinat 2D
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            background_line_style={"stroke_color": TEAL, "stroke_width": 1.5, "stroke_opacity": 0.3}
        )
        self.play(Create(plane))

        # 3. Kotak Satuan (Unit Square)
        square = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 0), plane.c2p(1, 1), plane.c2p(0, 1),
            fill_color=YELLOW, fill_opacity=0.35, stroke_color=YELLOW, stroke_width=2
        )
        square_lbl = Text("Area = 1", font_size=16, color=YELLOW).move_to(plane.c2p(0.5, 0.5))
        self.play(Create(square), FadeIn(square_lbl))

        # 4. Vektor Basis i-hat (hijau) dan j-hat (merah)
        v_i = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=GREEN_B, stroke_width=4)
        v_j = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=RED_B, stroke_width=4)
        lbl_i = Text("i-hat (1, 0)", font_size=16, color=GREEN_B).next_to(v_i.get_end(), DOWN, buff=0.1)
        lbl_j = Text("j-hat (0, 1)", font_size=16, color=RED_B).next_to(v_j.get_end(), LEFT, buff=0.1)
        self.play(GrowArrow(v_i), GrowArrow(v_j), Write(lbl_i), Write(lbl_j))
        self.wait(1)

        # 5. Label Matriks Transformasi
        mat_text = Text("T = [[ 1.5,  1.0 ], [ 0.5,  1.5 ]]", font_size=20, color=GREEN_A).to_corner(UL).shift(DOWN * 0.8)
        self.play(Write(mat_text), FadeOut(square_lbl), FadeOut(lbl_i), FadeOut(lbl_j))

        # 6. Transformasi Matriks (ApplyMatrix)
        matrix = [[1.5, 1.0], [0.5, 1.5]]
        self.play(
            plane.animate.apply_matrix(matrix),
            square.animate.apply_matrix(matrix),
            v_i.animate.apply_matrix(matrix),
            v_j.animate.apply_matrix(matrix),
            run_time=3
        )
        self.wait(1)

        # 7. Keterangan Determinan
        det_text = Text(
            "Det(T) = (1.5)(1.5) - (1.0)(0.5) = 1.75\nLuas Jajaran Genjang = 1.75 x Luas Awal",
            font_size=18,
            color=YELLOW
        ).to_corner(DL)
        self.play(Write(det_text))
        self.wait(2)
