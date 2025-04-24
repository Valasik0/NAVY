from tkinter import messagebox
import random

class TerrainController:
    def __init__(self):
        pass

    def draw_terrain(self, canvas, start_x, start_y, iterations, line_length, offset_num, color):
        start_x = self.validate_numeric_input(start_x)
        start_y = self.validate_numeric_input(start_y)
        iterations = self.validate_numeric_input(iterations)
        line_length = self.validate_numeric_input(line_length)
        offset_num = self.validate_numeric_input(offset_num)
        if None in (start_x, start_y, iterations, line_length, offset_num):
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            return
        
        iterations = int(iterations)

        points = [(start_x, start_y), (start_x + line_length, start_y)]   

        for _ in range(iterations):
            new_points = []
            for i in range(len(points) - 1):
                #get the start and end points of the current segment
                x1, y1 = points[i]
                x2, y2 = points[i + 1]

                #calculate the midpoint
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2

                #add random displacement to the midpoint
                displacement = random.uniform(-offset_num, offset_num)
                mid_y += displacement

                #add the new points to the list
                new_points.append((x1, y1))
                new_points.append((mid_x, mid_y))

            new_points.append(points[-1])  #add the last point
            points = new_points

        self.draw_on_canvas(points, color, canvas)
        
    def validate_numeric_input(self, input_value):
        try:
            value = float(input_value)
            return value
        except ValueError:
            return None
        
    def draw_on_canvas(self, points, color, canvas):
        canvas_height = int(canvas['height']) 
        filled_points = points + [(points[-1][0], canvas_height), (points[0][0], canvas_height)]

        canvas.create_polygon(
            *[coord for point in filled_points for coord in point],
            fill=color,
            outline=color 
        )

    def clear_canvas(self, canvas):
        canvas.delete("all")
