import tkinter as tk
from tkinter import colorchooser
from TerrainController import TerrainController

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fractal Terrain")
        self.root.geometry("800x600")
        self.canvas = None
        self.frame_left = tk.Frame(self.root)
        self.frame_right = tk.Frame(self.root)
        self.button_draw = None
        self.button_clear = None
        self.button_pick_color = tk.Button(self.frame_right, text="Pick Color", command=self.choose_color)
        self.color_chooser = None
        self.color = None
        self.textbox_start_x = None
        self.textbox_start_y = None
        self.textbox_x_end = None
        self.textbox_y_end = None
        self.textbox_offset_num = None
        self.textbox_iterations = None
        self.controller = TerrainController()

    
    def run(self):
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        self.canvas_component()
        self.controls_component()

        self.root.mainloop()

    def canvas_component(self):
        self.canvas = tk.Canvas(self.frame_left, width=600, height=600, bg="white")
        self.canvas.pack(pady=5)

    def choose_color(self):
        self.color_chooser = colorchooser.askcolor(title="Choose a color")
        if self.color_chooser:
            self.button_pick_color.config(bg=self.color_chooser[1])
            self.color = self.color_chooser[1]

    def controls_component(self):
        tk.Label(self.frame_right, text="Start X Position:").pack(pady=5, padx=10)
        self.textbox_start_x = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_start_x.pack(pady=(0, 20), padx=10)
        tk.Label(self.frame_right, text="Start Y Position:").pack(pady=5, padx=10)
        self.textbox_start_y = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_start_y.pack(pady=(0, 20), padx=10)
        tk.Label(self.frame_right, text="Iterations:").pack(pady=5, padx=10)
        self.textbox_iterations = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_iterations.pack(pady=(0, 20), padx=10)
        tk.Label(self.frame_right, text="X End Position:").pack(pady=5, padx=10)
        self.textbox_x_end = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_x_end.pack(pady=(0, 20), padx=10)
        tk.Label(self.frame_right, text="Y End Position:").pack(pady=5, padx=10)
        self.textbox_y_end = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_y_end.pack(pady=(0, 20), padx=10)
        tk.Label(self.frame_right, text="Offset Number:").pack(pady=5, padx=10)
        self.textbox_offset_num = tk.Text(self.frame_right, height=1, width=10)
        self.textbox_offset_num.pack(pady=(0, 20), padx=10)


        self.button_pick_color.pack(pady=5, padx=5)
        self.button_clear = tk.Button(self.frame_right, text="Clear", bg="pink", command=lambda: self.controller.clear_canvas(self.canvas))
        self.button_clear.pack(pady=5, padx=10)   
        self.button_draw = tk.Button(self.frame_right, text="Draw", font=("Arial", 16, "bold"), bg="lightblue"
                                     , command=lambda: self.controller.draw_terrain(
                                         self.canvas,
                                         self.textbox_start_x.get("1.0", tk.END).strip(),
                                         self.textbox_start_y.get("1.0", tk.END).strip(),
                                         self.textbox_iterations.get("1.0", tk.END).strip(),
                                         self.textbox_x_end.get("1.0", tk.END).strip(),
                                         self.textbox_y_end.get("1.0", tk.END).strip(),
                                         self.textbox_offset_num.get("1.0", tk.END).strip(),
                                         self.color))
        self.button_draw.pack(pady=5, padx=10)