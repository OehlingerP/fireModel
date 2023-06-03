# https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html

# manim index: https://docs.manim.community/en/stable/genindex.html
from manim import *
import csv

class GridToNetwork(Scene): # add name of class (GridToNetwork)
    def construct(self): # needed for every animation
        # Music by Daddy_s_Music from Pixabay
        self.add_sound("piano_adj.mp3")
        text = Text("The Fire Model").scale(1.5) # add texttext1.move_to([0, 3, 0])
        text.move_to([0, 1.5, 0])
        self.play( Write( text ), run_time=1 ) # self.play to animate and Write to have typesetting; run_time is self explaining

        text1 = Text("Changing the perspective").scale(0.5) # add text
        text1.move_to([0, 0.25, 0])
        self.play( Write( text1 ), run_time=1 ) 

        gr_text = VGroup( text, text1 )

        self.play( FadeOut( gr_text ) )

        text = Text("The Problem").scale(1) # add texttext1.move_to([0, 3, 0])
        text.move_to([0, 2, 0])
        self.play( Write( text ), run_time=1 ) # self.play to animate and Write to have typesetting; run_time is self explaining

        paraText = """
        To study the dynamics in the fire model simulations are needed.
        However, running the previous code hundreds of times would take
        ages. A more efficient code is needed.
        """

        text1 = Paragraph(paraText, alignment="left", line_spacing=0.5).scale(0.5) # add text
        text1.move_to([0, 0, 0])
        self.play( Write( text1 ), run_time=6 ) 

        gr_text = VGroup( text, text1 )

        self.wait()

        self.play( FadeOut( gr_text ) )

        # add explanation
        text1 = Text( "Start with a randomly populated forest" ).scale(0.5)
        text2 = Text( "(1's indicate trees)").scale(0.4)
        text1.move_to([0, 3, 0])
        text2.move_to([0, 2.5, 0])
        self.play( Write( text1 ), run_time=0.75 )
        self.play( Write( text2 ), run_time=0.75 )

        gr_text = VGroup( text1, text2 )

        mat = Matrix([[1, 0, 0, 1], 
                      [1, 1, 1, 0],
                      [0, 0, 1, 0],
                      [1, 1, 0, 1]])
        
        # populate matrix
        self.play( Write( mat ) )

        self.play( FadeOut( gr_text ) )

        # color connected components
        # Function to highlight a cell in the matrix
        def highlight_cell(mat, entry, color, runTime):
            entries = mat.get_entries()
            ent = entries[entry]
            ent.set_color(color)
            self.play(Write(ent), run_time = runTime )

        text3 = Text( "Wildfire spreads from left to right" ).scale(0.5)
        text3.move_to([0, 3, 0])
        self.play( Write( text3 ), run_time=0.75 ) 

        colour = RED
        rT = 0.3
        # Example usage: highlight the first element in the matrix
        entries = mat.get_entries()
        ent = VGroup( entries[0], entries[4], entries[12] )
        ent.set_color(colour)
        self.play(Write(ent), run_time = rT )
        entries = mat.get_entries()
        ent = VGroup( entries[5], entries[13] )
        ent.set_color(colour)
        self.play(Write(ent), run_time = rT )
        highlight_cell(mat, 6, colour, rT)
        highlight_cell(mat, 10, colour, rT)

        self.play( FadeOut( text3 ) )

        text3 = Text( "Instead of a binary matrix we can consider this matrix as a network of connected trees." ).scale(0.5)
        text3.move_to([0, 3, 0])
        self.play( Write( text3 ), run_time=0.75 ) 

        #mat.to_edge( LEFT )
        self.play(mat.animate.to_edge(LEFT), run_time = 0.25)
        self.wait()

        arrow = Arrow(LEFT, RIGHT)

        self.play(Create(arrow))

        # create matrix of circles
        space = 0.8
        rad = 0.25
        col_burn = RED
        col_norm = GREEN
        circ_opa = 0.25

        node1 = Circle(radius=rad, color=col_burn, fill_color = col_burn, fill_opacity = circ_opa)
        node2 = Circle(radius=rad, color=col_burn, fill_color = col_burn, fill_opacity = circ_opa)
        node3 = Circle(radius=rad, color=col_norm, fill_color = col_norm, fill_opacity = circ_opa)
        node4 = Circle(radius=rad, color=col_norm, fill_color = col_norm, fill_opacity = circ_opa)
        node5 = Circle(radius=rad, color=col_norm, fill_color = col_norm, fill_opacity = circ_opa)
        node6 = Circle(radius=rad, color=col_burn, fill_color = col_burn, fill_opacity = circ_opa)
        node7 = Circle(radius=rad, color=col_norm, fill_color = col_norm, fill_opacity = circ_opa)

        node8 = Circle(radius=rad, color=WHITE, fill_color = WHITE, fill_opacity = circ_opa)
        node9 = Circle(radius=rad, color=WHITE, fill_color = WHITE, fill_opacity = circ_opa)

        # Position the circle
        node1.move_to([0 * space, 2 * space, 0]) # 0 0
        node2.move_to([0 * space, 1 * space, 0])
        node3.move_to([1 * space, 1 * space, 0])
        node4.move_to([2 * space, 1 * space, 0])
        node5.move_to([2 * space, 0 * space, 0])
        node6.move_to([0 * space, -1 * space, 0])
        node7.move_to([1 * space, -1 * space, 0])

        node8.move_to([3 * space, 2 * space, 0])
        node9.move_to([3 * space, -1 * space, 0])

        gr = VGroup(node1, node2, node3, 
                    node4, node5, node6, 
                    node7, node8, node9 )

        #gr.shift(DOWN * 0.3)
        #gr.shift(RIGHT * 3 )
        gr.move_to( [3, -0.2, 0] )
        self.play( Write( gr ) )

        # combine nodes by lines
        pos1 = node1.get_bottom()
        pos2 = node2.get_top()
        line12 = Line(pos1, pos2, color = col_burn)

        pos1 = node6.get_right()
        pos2 = node7.get_left()
        line67 = Line(pos1, pos2, color = col_burn)

        pos1 = node2.get_right()
        pos2 = node3.get_left()
        line23 = Line(pos1, pos2, color = col_burn)

        rT = 0.15
        gr_line = VGroup( line12, line67, line23 )
        self.play(Write(gr_line), run_time = rT)

        # Change the color of the circle
        gr_node67 = VGroup( node3, node7 )

        self.play( gr_node67.animate.set_fill(col_burn), run_time = rT )
        self.play( gr_node67.animate.set_color(col_burn), run_time = rT )

        pos1 = node3.get_right()
        pos2 = node4.get_left()
        line34 = Line(pos1, pos2, color = col_burn)
        self.play(Write(line34), run_time = rT)

        self.play( node4.animate.set_fill(col_burn), run_time = rT )
        self.play( node4.animate.set_color(col_burn), run_time = rT )

        pos1 = node4.get_bottom()
        pos2 = node5.get_top()
        line45 = Line(pos1, pos2, color = col_burn)
        self.play(Write(line45), run_time = rT)

        self.play( node5.animate.set_fill(col_burn), run_time = rT )
        self.play( node5.animate.set_color(col_burn), run_time = rT )

        self.play( FadeOut( text3 ) )

        text1 = Text( "The total area burned is then just the size of the two red components." ).scale(0.5)
        text1.move_to([0, 3, 0])
        text2 = Text( "Graph theory offers efficient algorithms to calculate them.").scale(0.35)
        text2.move_to([0, 2.5, 0])
        self.play(Write(text1), run_time=2)
        self.play(Write(text2), run_time=2)

        #text3 = Text( "Finding the graph representation of a binary matrix is the tricky part.").scale(0.35)
        #text3.move_to([0, -2.5, 0])
        #self.play( Write( text3 ), run_time=2 )

        self.wait()

        # Fade out all objects in the scene
        self.play(
            *[FadeOut(mob)for mob in self.mobjects] # All mobjects in the screen are saved in self.mobjects
        )

        text1 = Text( "Let's run the simulations and see what happens" ).scale(0.5)
        text1.move_to([0, 3, 0])
        text2 = Text( "The goal is to study the behavior of the fire model by varying the tree denstiy parameter.").scale(0.35)
        text2.move_to([0, 2.5, 0])
        self.play(Write(text1), run_time=2)
        self.play(Write(text2), run_time=2)

        blist = BulletedList("Randomly populate a matrix for a given tree density.",
                             "Find the network representation of the binary matrix.",
                             "Find the size of the components bordering the fire line and calculate the area burned.",
                             "Loop over steps one to three 100 times.",
                             "Repeat for each tree density from 1 to 100.", height=4, width=8)
        self.play(AddTextWordByWord(blist), run_time = 6 )
        self.wait(3)


        gr_text = VGroup( text1, text2, blist)
        self.play( FadeOut( gr_text ) )

        axes = Axes(
            x_range=(0, 109, 10),
            y_range=(0, 109 , 10),
            x_length=8,
            y_length=6,
            axis_config={
                "include_tip": True,
                "include_ticks": True,
            }
        )

        # Load data from CSV file
        points_data = []

        with open('data_all.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                x, y = map(float, row)
                points_data.append((x, y))

        points = VGroup(*[Dot(axes.c2p(x, y), color=RED).scale(0.2) for x, y in points_data])

        labels = axes.get_axis_labels(
            Text("Tree Density [%]").scale(0.4), Text("Total Area Burned [%]").scale(0.4)
        )

        self.play(Write(axes))
        self.play(Write(labels))
        self.play(Write(points), run_time = 2) 
        text = Text("Phase transition at around 60% tree density.").scale(0.35)
        text.move_to([3, 0, 0])
        self.play( Write( text ), run_time=2 )
        self.wait(2.5)

class Test(Scene):
    def construct(self):
        self.add_sound("piano.mp3")
        axes = Axes(
            x_range=(0, 109, 10),
            y_range=(0, 111, 10),
            x_length=8,
            y_length=6,
            axis_config={
                "include_tip": True,
                "include_ticks": True,
            }
        )

        points_data = [
            (1, 2),
            (20, 10),
            (40, 15),
            (60, 80),
            (100, 100)
        ]

        # Load data from CSV file
        #points_data = []

        #with open('data_all.csv', 'r') as file:
        #    reader = csv.reader(file)
        #    for row in reader:
        #        x, y = map(float, row)
        #        points_data.append((x, y))

        points = VGroup(*[Dot(axes.c2p(x, y), color=RED).scale(0.2) for x, y in points_data])

        labels = axes.get_axis_labels(
            Text("Tree Density [%]").scale(0.4), Text("Total Area Burned [%]").scale(0.4)
        )


        self.play(Write(axes))
        self.play(Write(labels))
        self.play(Write(points)) 
        text = Text("Phase transition at around 60% tree density.").scale(0.35)
        text.move_to([3, 0, 0])
        self.play( Write( text ), run_time=2 )
        self.wait(2.5)