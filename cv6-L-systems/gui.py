import tkinter as tk
from tkinter import messagebox
from lsystemsController import LSystemsController
from presets import first, second, third, forth

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("L-Systems")
        self.root.geometry("1050x600")
        self.frame_left = None
        self.frame_right = None
        self.frame_start_controls = None
        self.frame_custom = None
        self.ib_pos_x = None
        self.ib_pos_y = None
        self.ib_start_angle = None
        self.ib_line_length = None
        self.ib_nesting_num = None
        self.btn_draw_fst = None
        self.btn_draw_snd = None
        self.btn_draw_thrd = None
        self.btn_draw_frth = None
        self.ib_axiom = None
        self.ib_rule = None
        self.ib_custome_angle = None
        self.chb_start_radians = None
        self.chb_custom_radians = None
        self.radians = False
        self.controller = LSystemsController()
    
    def run(self):
        self.frame_left = tk.Frame(self.root)
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10)
        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

        self.canvas_component()
        self.start_controls_component()
        self.draw_saved_component()
        self.custom_component()

        self.root.mainloop()

    def toggle_radians(self):
        if self.chb_start_radians.var.get():
            self.radians = True
        else:
            self.radians = False
    
    def start_controls_component(self):
        self.chb_start_radians = tk.Checkbutton(self.frame_right, text="Radians", variable=tk.BooleanVar(), onvalue=True, offvalue=False, command=self.toggle_radians)
        self.chb_start_radians.grid(row=1, column=0, pady=10)

        self.frame_start_controls = tk.Frame(self.frame_right, border=1, relief=tk.SUNKEN)
        self.frame_start_controls.grid(row=0, column=0, padx=10, pady=10)
        
        tk.Label(self.frame_start_controls, text="Start X Position:").pack(pady=5)   
        self.ib_pos_x = tk.Text(self.frame_start_controls, height=1, width=10)
        self.ib_pos_x.pack(pady=(0, 20))

        tk.Label(self.frame_start_controls, text="Start Y Position:").pack(pady=5)
        self.ib_pos_y = tk.Text(self.frame_start_controls, height=1, width=10)
        self.ib_pos_y.pack(pady=(0, 20))

        tk.Label(self.frame_start_controls, text="Start Angle:").pack(pady=5)
        self.ib_start_angle = tk.Text(self.frame_start_controls, height=1, width=10)
        self.ib_start_angle.pack(pady=(0, 5))


        tk.Label(self.frame_start_controls, text="Number of nesting:").pack(pady=5)
        self.nesting_num = tk.Text(self.frame_start_controls, height=1, width=10)
        self.nesting_num.pack(pady=(0, 20))

        tk.Label(self.frame_start_controls, text="Line lenght (px):").pack(pady=5)
        self.line_length = tk.Text(self.frame_start_controls, height=1, width=10)
        self.line_length.pack(pady=(0, 20))

    def draw_saved_component(self):
        self.btn_draw_fst = tk.Button(self.frame_start_controls, text="Draw 1st",bg="lightgreen")
        self.btn_draw_fst.pack(pady=5, fill=tk.X)

        self.btn_draw_snd = tk.Button(self.frame_start_controls, text="Draw 2nd",bg="lightgreen")
        self.btn_draw_snd.pack(pady=5, fill=tk.X)

        self.btn_draw_thrd = tk.Button(self.frame_start_controls, text="Draw 3rd",bg="lightgreen")
        self.btn_draw_thrd.pack(pady=5, fill=tk.X)

        self.btn_draw_frth = tk.Button(self.frame_start_controls, text="Draw 4th",bg="lightgreen")
        self.btn_draw_frth.pack(pady=5, fill=tk.X)
    
    def custom_component(self):
        self.frame_custom = tk.Frame(self.frame_right, border=1, relief=tk.SUNKEN)
        self.frame_custom.grid(row=0, column=1, padx=60, pady=10)

        tk.Label(self.frame_custom, text="Custom L-System:", font=("Arial", 14, "bold")).pack(pady=5)

        tk.Label(self.frame_custom, text="Axiom").pack(pady=5)
        self.ib_axiom = tk.Text(self.frame_custom, height=1, width=10)
        self.ib_axiom.pack(pady=(0, 20))

        tk.Label(self.frame_custom, text="Rule").pack(pady=5)
        self.ib_rule = tk.Text(self.frame_custom, height=1, width=10)
        self.ib_rule.pack(pady=(0, 20))

        tk.Label(self.frame_custom, text="Angle").pack(pady=5)
        self.ib_custome_angle = tk.Text(self.frame_custom, height=1, width=10)
        self.ib_custome_angle.pack(pady=(0, 20))

        self.btn_draw_custom = tk.Button(self.frame_custom, text="Draw custom", bg="lightgreen", 
                                         command=lambda: self.controller.draw_custom(self.ib_axiom.get("1.0", tk.END).strip(), 
                                                                                     self.ib_rule.get("1.0", tk.END).strip(), 
                                                                                     self.ib_custome_angle.get("1.0", tk.END).strip(),
                                                                                     self.canvas,
                                                                                     float(self.ib_pos_x.get("1.0", tk.END).strip()),
                                                                                     float(self.ib_pos_y.get("1.0", tk.END).strip()),
                                                                                     float(self.line_length.get("1.0", tk.END).strip()),
                                                                                     int(self.nesting_num.get("1.0", tk.END).strip()),
                                                                                     float(self.ib_start_angle.get("1.0", tk.END).strip()),
                                                                                     self.radians),
                                                                                     )
        
        self.btn_draw_custom.pack(pady=5, fill=tk.X)

        self.btn_clear = tk.Button(self.frame_custom, text="Clear grid", bg="pink", command=lambda: self.controller.clear_canvas(self.canvas))
        self.btn_clear.pack(pady=5, fill=tk.X)



    def canvas_component(self):
        self.canvas = tk.Canvas(self.frame_left, width=600, height=600, bg="white")
        self.canvas.pack(pady=5)

        self.canvas.create_line(100, 100, 200, 200, fill="black", width=1)