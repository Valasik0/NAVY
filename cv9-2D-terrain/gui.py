import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Fractal Terrain")
        self.root.geometry("1050x600")
        self.canvas = None
        self.frame_left = None
        self.frame_right = None
    
    def run(self):
        self.frame_left = tk.Frame(self.root)
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        self.canvas_component()
        self.start_controls_component()

        self.root.mainloop()

    def canvas_component(self):
        self.canvas = tk.Canvas(self.frame_left, width=600, height=600, bg="white")
        self.canvas.pack(pady=5)

    def start_controls_component(self):
        pass    