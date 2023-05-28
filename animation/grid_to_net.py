# https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeOut.html
from manim import *

class GridToNetwork(Scene): # add name of class (GridToNetwork)
    def construct(self): # needed for every animation
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
        ages. A more efficient code is needed. In this video, I will 
        just present the idea.
        """

        text1 = Paragraph(paraText, alignment="left", line_spacing=0.5).scale(0.75) # add text
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

        # populate matrix row by row
        # self.add(mat.get_brackets()) # add brackets before populating
        # rows = mat.get_rows()
        # self.play(Write(rows[0]))
        # self.play(Write(rows[1]))
        # self.play(Write(rows[2]))
        # self.play(Write(rows[3]))

        # color connected entries
        #entries = mat.get_entries()
        #colors = [RED, WHITE, WHITE, WHITE, RED, RED, RED, WHITE, WHITE, WHITE, RED, WHITE, RED, RED, WHITE, WHITE]
        #for k in range(len(colors)):
        #    entries[k].set_color(colors[k])
        #self.play( Write( mat ) )

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
        self.play(mat.animate.to_edge(LEFT))
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
        self.play( Write( text1 ), run_time=2 )
        self.play( Write( text2 ), run_time=2 )

        text3 = Text( "Finding the graph representation of a binary matrix is the tricky part we will look at.").scale(0.35)
        text3.move_to([0, -2.5, 0])
        self.play( Write( text3 ), run_time=2 )

        self.wait()

        # Fade out all objects in the scene
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        self.wait()

import numpy as np

class RandomMatrix2(Scene):
    def construct(self):
        # Set matrix dimensions
        rows, cols = 50, 50
        # Generate random binary matrix
        matrix = np.random.choice([0, 1], size=(rows, cols), p=[0.9, 0.1])
        mat = Matrix( matrix, v_buff = 0.2, h_buff = 0.2)
        self.add(mat)
        self.wait()

class RandomMatrix(Scene):
    def construct(self):
        # Set matrix dimensions
        rows, cols = 50, 50
        
        square_size = 0.1
        gap_size = 0
        # Generate random binary matrix
        matrix = np.random.choice([0, 1], size=(rows, cols), p=[0.9, 0.1])
        


        # Create squares to represent matrix elements
        squares = VGroup()
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=square_size)
                square.move_to([i-(rows-1)/2 * (square_size + gap_size), j-(cols-1)/2 * (square_size + gap_size), 0])
                if matrix[i][j] == 1:
                    square.set_fill(RED, opacity=1)
                else:
                    square.set_fill(WHITE, opacity=1)
                squares.add(square)
        
        # Add squares to the scene
        self.add(squares)
        self.wait()

import numpy as np

class VaryingProbMatrix(Scene):
    def construct(self):
        # Set matrix dimensions
        rows, cols = 50, 50
        
        # Define the range of probabilities
        min_prob, max_prob = 0.01, 1
        num_steps = 100
        
        # Compute the step size
        step_size = (max_prob - min_prob) / num_steps
        
        # Iterate over the range of probabilities
        for i in range(num_steps + 1):
            # Compute the current probability
            current_prob = min_prob + i * step_size
            
            # Generate random binary matrix
            matrix = np.random.choice([0, 1], size=(rows, cols), p=[1-current_prob, current_prob])
            
            # Create squares to represent matrix elements
            squares = VGroup()
            for i in range(rows):
                for j in range(cols):
                    square = Square(side_length=0.1)
                    square.move_to([i-rows/2 + 0.1/2, j-cols/2 + 0.1/2, 0])
                    if matrix[i][j] == 1:
                        square.set_fill(RED, opacity=1)
                    else:
                        square.set_fill(WHITE, opacity=1)
                    squares.add(square)
            
            # Add squares to the scene and wait for a short duration
            self.add(squares)
            self.wait(0.1)
            
            # Remove squares from the scene
            self.remove(squares)

import pandas as pd

class ScatterPlot(Scene):
    def construct(self):
        # Load data from CSV file
        data = pd.read_csv("data.csv")
        
        # Create scatter plot points
        points = VGroup()
        for _, row in data.iterrows():
            point = Dot().move_to([row['variable'], row['mean'], 0])
            points.add(point)
        
        # Create axes
        axes = Axes(
            x_range=[0, 105, 10],
            y_range=[0, 105, 10],
            x_length=8,
            y_length=6
        )
        
        # Add scatter plot points to the scene
        self.add(axes, points)
        
        # Animate the scatter plot points
        self.play(AnimationGroup(*[FadeIn(p) for p in points]))
        self.wait()


