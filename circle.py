from manim import *

class DivideCircle(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        self.add(circle)
        self.wait()

        center = circle.get_center()
        for i in range(8):
            angle = i * TAU / 8
            x = center[0] + 2 * np.cos(angle)
            y = center[1] + 2 * np.sin(angle)
            point = [x, y, 0]
            line = Line(center, point, color=WHITE)
            self.play(Write(line))
        self.wait()
        self.clear()
        self.wait()
        sector1 = Sector(radius=2, start_angle=PI/4,angle=PI/2, color=RED)
        sector2 = Sector(radius=2, start_angle=PI/4,angle=PI/2, color=BLUE)
        sector3 = Sector(radius=2, start_angle=PI/4,angle = PI/2, color=GREEN)
        sector4 = Sector(radius=2, start_angle=PI/4,angle = PI/2, color=YELLOW)

        sector2.next_to(sector1, direction=RIGHT, buff=0)
        sector3.next_to(sector2, direction=RIGHT, buff=0)
        sector4.next_to(sector3, direction=RIGHT, buff=0)



        self.add(sector1, sector2, sector3, sector4)
        self.wait()

        sector5 = Sector(radius=2, start_angle=PI/4,angle=PI/2, color=RED)
        sector6 = Sector(radius=2, start_angle=PI/4,angle=PI/2, color=BLUE)
        sector7 = Sector(radius=2, start_angle=PI/4,angle = PI/2, color=GREEN)
        sector8 = Sector(radius=2, start_angle=PI/4,angle = PI/2, color=YELLOW)

        sector5.shift((-0.7,-0.3,0))
        sector6.next_to(sector5, direction=RIGHT, buff=0)
        sector7.next_to(sector6, direction=RIGHT, buff=0)
        sector8.next_to(sector7, direction=RIGHT, buff=0)
        self.add(sector5, sector6, sector7, sector8)
        self.play(
            Rotate(sector5, angle=PI), 
            Rotate(sector6, angle=PI), 
            Rotate(sector7, angle=PI), 
            Rotate(sector8, angle=PI)
            )
        self.wait()
        self.clear()

        sector1 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=RED)
        sector2 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=BLUE)
        sector3 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=GREEN)
        sector4 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=YELLOW)
        sector5 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=RED)
        sector6 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=BLUE)
        sector7 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=GREEN)
        sector8 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=YELLOW)

        sector1_2 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=RED)
        sector2_2 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=BLUE)
        sector3_2 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=GREEN)
        sector4_2 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=YELLOW)
        sector5_2 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=RED)
        sector6_2 = Sector(radius=2, start_angle=7*PI/16,angle=PI/8, color=BLUE)
        sector7_2 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=GREEN)
        sector8_2 = Sector(radius=2, start_angle=7*PI/16,angle =PI/8, color=YELLOW)
        #PI/8 22,5 7PI/16 78,75
        self.wait()

        self.add(sector1, sector2, sector3, sector4, sector5, sector6, sector7, sector8)
        self.add(sector1_2, sector2_2, sector3_2, sector4_2, sector5_2, sector6_2, sector7_2, sector8_2)
        sector1.shift((-0.2,-0.05,0))
        sector2.next_to(sector1, direction=RIGHT, buff=0)
        sector3.next_to(sector2, direction=RIGHT, buff=0)
        sector4.next_to(sector3, direction=RIGHT, buff=0)
        sector5.next_to(sector4, direction=RIGHT, buff=0)
        sector6.next_to(sector5, direction=RIGHT, buff=0)
        sector7.next_to(sector6, direction=RIGHT, buff=0)
        sector8.next_to(sector7, direction=RIGHT, buff=0)

        sector2_2.next_to(sector1_2, direction=RIGHT, buff=0)
        sector3_2.next_to(sector2_2, direction=RIGHT, buff=0)
        sector4_2.next_to(sector3_2, direction=RIGHT, buff=0)
        sector5_2.next_to(sector4_2, direction=RIGHT, buff=0)
        sector6_2.next_to(sector5_2, direction=RIGHT, buff=0)
        sector7_2.next_to(sector6_2, direction=RIGHT, buff=0)
        sector8_2.next_to(sector7_2, direction=RIGHT, buff=0)

        self.play(
            Rotate(sector1, angle=PI), 
            Rotate(sector2, angle=PI), 
            Rotate(sector3, angle=PI), 
            Rotate(sector4, angle=PI),
            Rotate(sector5, angle=PI),
            Rotate(sector6, angle=PI),
            Rotate(sector7, angle=PI),
            Rotate(sector8, angle=PI)
            )
        
        thegoal1 = Tex("A coisa aqui é que, quanto mais vezes a gente corta o círculo,").to_edge(UP, buff=1)
        thegoal2 = Tex("mais a forma parece um retângulo").to_edge(UP, buff=2)
        self.play(Write(thegoal1), Write(thegoal2))
        self.wait()