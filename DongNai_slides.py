from manim import *
from manim_slides import Slide
import numpy as np
config.tex_template.add_to_preamble("\\usepackage[utf8]{vietnam}")
config.tex_template.add_to_preamble("\\usepackage{pifont}")
class Bai1(Slide):

    def construct(self):
        debai = Tex(r"Giải phương trình").to_corner(UP).scale(0.6)
        equationA = MathTex(*r'2  x^2  -7  x  +6  =  0'.split('  ')).shift(4*LEFT+2*UP).scale(0.6)
        duong2 = equationA[0].copy().set_color(BLUE)
        am7 = equationA[2].copy().set_color(RED)
        duong6 = equationA[4][1].copy().set_color(YELLOW)
        line = Line(2*UP , 2*DOWN).set_color(WHITE).shift(0.2*RIGHT)
        buocgiai = Tex(r"""
                   \begin{description}
                   \item Các bước giải phương trình bậc hai $ax^2+bx+c=0$.
                   \item Bước 1. Tính $\Delta$
                   \item Bước 2. Kết luận về nghiệm của phương trình dựa vào dấu của $\Delta$
                   \begin{itemize}
                   \item[\ding{82}] Nếu $\Delta >0$ thì phương trình có hai nghiệm phân biệt 
                   \[ x_1 = \frac{-b-\sqrt{\Delta}}{2a}, x_2=\frac{-b+\sqrt{\Delta}}{2a}. \]
                   \item[\ding{82}] Nếu $\Delta =0$ thì phương trình có nghiệm kép $x=-\dfrac{b}{2a}$.
                   \item[\ding{82}] Nếu $\Delta <0$ thì phương trình vô nghiệm.
                   \end{itemize}
                   \end{description}
                   """,
                   tex_environment = "{minipage}{23em}"
                   ).scale(0.5).to_corner(RIGHT)
        self.play(Write(debai))
        self.play(Write(equationA))
        self.next_slide()
        self.play(Create(line))
        self.play(Write(buocgiai))
        self.next_slide()
        contro = Tex(r'\ding{43}').scale(0.7).next_to(buocgiai[0][39], LEFT, buff=0.1)
        self.play(FadeIn(contro), 
                  buocgiai[0][39:50].animate.set_color(BLUE_B), 
                  Wiggle(buocgiai[0][39:50]), 
                  buocgiai[0][50:].animate.set_opacity(0.5))
        self.next_slide()
        self.play(equationA[0].animate.set_color(BLUE), Wiggle(equationA[0]),lag_ratio=0.5) # hệ số a
        self.play(equationA[2].animate.set_color(RED), Wiggle(equationA[2]),lag_ratio=0.5) #hệ số b
        self.play(equationA[4].animate.set_color(YELLOW), Wiggle(equationA[4]),lag_ratio=0.5) #hệ số c
        deltaA= MathTex(*r'\Delta  =  b  ^2  -  4  \cdot  a  \cdot  c'.split('  ')).next_to(equationA, DOWN).scale(0.6)
        
        deltaA[2].set_color(RED) #b trong delta
        deltaA[7].set_color(BLUE) #a trong delta
        deltaA[9].set_color(YELLOW) #c trong delta

        leftbracket=MathTex('(').shift(deltaA[2].get_center()).scale(0.6)
        rightbracket=MathTex(')').shift(deltaA[2].get_center()).scale(0.6)

        self.play(Write(deltaA))
        self.next_slide()
        self.play(
            am7.animate.shift(deltaA[2].get_center()-equationA[2].get_center()),
            FadeOut(deltaA[2]),
            FadeIn(leftbracket),
            leftbracket.animate.shift(0.3*LEFT),
            FadeIn(rightbracket),
            rightbracket.animate.shift(0.3*RIGHT),
            deltaA[3:].animate.shift(0.4*RIGHT),
            deltaA[:2].animate.shift(0.3*LEFT)
        )
        self.play(
            duong2.animate.shift(deltaA[7].get_center()-equationA[0].get_center()),
            FadeOut(deltaA[7])
            )
        self.play(
            duong6.animate.shift(deltaA[9].get_center()-equationA[4][1].get_center()),
            FadeOut(deltaA[9])
            )
        self.next_slide()
        ketquadeltaA= MathTex('=1').scale(0.6).next_to(deltaA[9].get_right(), RIGHT, buff=0.15)
        self.play(Create(ketquadeltaA))
        self.next_slide()
        self.play(contro.animate.next_to(buocgiai[0][50].get_left(), LEFT, buff=0.1), 
                  Wiggle(buocgiai[0][50:]), 
                  buocgiai[0][39:50].animate.set_color(WHITE).set_opacity(0.5),
                  buocgiai[0][50:].animate.set_opacity(1).set_color(BLUE_B)
                  )
        self.next_slide()
        bienluan=Tex(r'Vì $\Delta>0$ nên phương trình có hai nghiệm phân biệt').scale(0.6).next_to(deltaA, DOWN).shift(0.3*RIGHT)
        hainghiem=MathTex(r'x_1 = \frac{- \quad b \quad - \sqrt{\Delta}}{2 \cdot a}, x_2=\frac{- \quad b \quad +\sqrt{\Delta}}{2 \cdot a}.').scale(0.6).next_to(deltaA, DOWN, buff=0.8)
        self.play(Write(bienluan))
        self.play(Write(hainghiem))
        self.next_slide()
        tru7 = VGroup(equationA[2].copy().set_color(RED), leftbracket.copy().next_to(equationA[2], LEFT, buff=0.05), rightbracket.copy().next_to(equationA[2], RIGHT, buff=0.05))
        tru7_2 = VGroup(equationA[2].copy().set_color(RED), leftbracket.copy().next_to(equationA[2], LEFT, buff=0.05), rightbracket.copy().next_to(equationA[2], RIGHT, buff=0.05))
        cong1 = ketquadeltaA[0][1].copy()
        cong1_2 = ketquadeltaA[0][1].copy()
        cong2 = equationA[0].copy().set_color(BLUE)
        cong2_2 = equationA[0].copy().set_color(BLUE)
    
        leftbracket2=MathTex('(').next_to(deltaA[2].get_center()).scale(0.6)
        rightbracket2=MathTex(')').shift(deltaA[2].get_center()).scale(0.6)
        self.play(
            tru7.animate.shift(hainghiem[0][4].get_center()-equationA[2].get_center()),
            FadeOut(hainghiem[0][4]),
            tru7_2.animate.shift(hainghiem[0][18].get_center()-equationA[2].get_center()),
            FadeOut(hainghiem[0][18])
        )
        
        self.play(
            cong1.animate.shift(hainghiem[0][8].get_center()-ketquadeltaA[0][1].get_center()),
            FadeOut(hainghiem[0][8]),
            cong1_2.animate.shift(hainghiem[0][22].get_center()-ketquadeltaA[0][1].get_center()),
            FadeOut(hainghiem[0][22])
        )
        self.play(
            cong2.animate.shift(hainghiem[0][12].get_center()-equationA[0].get_center()).align_to(hainghiem[0][10], UP),
            FadeOut(hainghiem[0][12]),
            cong2_2.animate.shift(hainghiem[0][26].get_center()-equationA[0].get_center()).align_to(hainghiem[0][24], UP),
            FadeOut(hainghiem[0][26])
        )
        ketquanghiem1 = MathTex(r'=\frac{3}{2}').scale(0.6).next_to(hainghiem[0][9], RIGHT, buff=0.01).shift(0.15*LEFT)
        ketquanghiem2 = MathTex(r'=2').scale(0.6).next_to(hainghiem[0][23], RIGHT, buff=0.48)
        self.next_slide()
        for i in [4,8,12, 18, 22, 26]: hainghiem[0][i].set_opacity(0) 
        self.play(
            hainghiem[0][:12].animate.shift(0.3*LEFT),
            tru7.animate.shift(0.3*LEFT),
            cong1.animate.shift(0.3*LEFT),
            cong2.animate.shift(0.3*LEFT),
            Write(ketquanghiem1),
            hainghiem[0][13:27].animate.shift(0.4*RIGHT),
            hainghiem[0][27].animate.shift(0.9*RIGHT),
            tru7_2.animate.shift(0.4*RIGHT),
            cong1_2.animate.shift(0.4*RIGHT),
            cong2_2.animate.shift(0.4*RIGHT),
            Write(ketquanghiem2)
        )
        self.next_slide()
        ketluan = Tex(r'Vậy phương trình có hai nghiệm $x_1=\dfrac{3}{2}$, $x_2 = 2$.').scale(0.6).next_to(hainghiem, DOWN)
        self.play(Write(ketluan))
        self.next_slide()
        rectangle=Rectangle(height=3.1, width=7, color=YELLOW).move_to(np.array([-3.6, 0.2, 0]))
        self.play(Create(rectangle))
        self.play(buocgiai.animate.set_color(WHITE).set_opacity(1), FadeOut(contro))


