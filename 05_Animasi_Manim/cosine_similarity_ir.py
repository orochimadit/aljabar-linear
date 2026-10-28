"""
================================================================================
ANIMASI MANIM: COSINE SIMILARITY / MESIN PENCARI (ALGEO 00)
Mata Kuliah : Aljabar Linier & Geometri — UNU Kalbar
Dosen       : Aditya Pratama
Referensi   : Rinaldi Munir (STEI ITB) & 3Blue1Brown
================================================================================
Cara Menjalankan (Render Video MP4):
  manim -pql cosine_similarity_ir.py AnimasiCosineSimilarity
================================================================================
"""

from manim import *

class AnimasiCosineSimilarity(Scene):
    def construct(self):
        # 1. Judul Perkuliahan UNU Kalbar
        header = Text("Aplikasi Algeo: Mesin Pencari & Cosine Similarity", font_size=28, color=BLUE_B).to_edge(UP)
        dosen = Text("UNU Kalbar • Dosen: Aditya Pratama", font_size=16, color=GRAY_B).next_to(header, DOWN, buff=0.1)
        self.play(Write(header), FadeIn(dosen))
        self.wait(1)

        # 2. Sumbu Koordinat Bidang Vektor
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": BLUE_C},
        ).shift(DOWN * 0.5 + LEFT * 1.5)

        x_label = Text("Kata: 'Aljabar'", font_size=16, color=GRAY_B).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("Kata: 'Geometri'", font_size=16, color=GRAY_B).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # 3. Vektor Kueri Q (3, 4)
        v_query = Arrow(axes.c2p(0, 0), axes.c2p(3, 4), buff=0, color=YELLOW, stroke_width=4)
        lbl_query = MathTex(r"Q = (3, 4)", font_size=22, color=YELLOW).next_to(v_query.get_end(), UR, buff=0.1)

        self.play(GrowArrow(v_query), Write(lbl_query))
        self.wait(1)

        # 4. Vektor Dokumen D1 (1, 5) dan Dokumen D2 (5, 1)
        v_doc1 = Arrow(axes.c2p(0, 0), axes.c2p(1, 5), buff=0, color=GREEN_B, stroke_width=3.5)
        lbl_doc1 = MathTex(r"D_1 = (1, 5)", font_size=20, color=GREEN_B).next_to(v_doc1.get_end(), UL, buff=0.1)

        v_doc2 = Arrow(axes.c2p(0, 0), axes.c2p(5, 1), buff=0, color=RED_B, stroke_width=3.5)
        lbl_doc2 = MathTex(r"D_2 = (5, 1)", font_size=20, color=RED_B).next_to(v_doc2.get_end(), DR, buff=0.1)

        self.play(GrowArrow(v_doc1), Write(lbl_doc1))
        self.play(GrowArrow(v_doc2), Write(lbl_doc2))
        self.wait(1)

        # 5. Panel Formula dan Penjelasan di Sebelah Kanan
        formula_box = VGroup(
            MathTex(r"\cos \theta = \frac{Q \cdot D}{\|Q\| \|D\|}", font_size=26, color=YELLOW),
            Text("Semakin kecil sudut θ,", font_size=16, color=WHITE),
            Text("semakin tinggi nilai cos θ,", font_size=16, color=GREEN_B),
            Text("semakin relevan dokumen!", font_size=16, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT, buff=0.8).shift(UP * 0.2)

        box_rect = SurroundingRectangle(formula_box, color=BLUE_D, buff=0.25, fill_color="#0b1120", fill_opacity=0.8)

        self.play(Create(box_rect), Write(formula_box))
        self.wait(3)
