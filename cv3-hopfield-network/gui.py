import tkinter as tk

class GUI:
    def __init__(self):
        self.components = []
        self.root = tk.Tk()
        self.root.title("Hopfield network")
        self.root.geometry("550x400")
        self.grid_buttons = []
        self.save_btn = None
        self.show_saved_btn = None
        self.clear_btn = None
        self.sync_repair_btn = None
        self.async_repair_btn = None
        self.left_frame = None
        self.right_frame = None
        

    def run(self):
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.grid_component()
        self.buttons_component()

        self.root.mainloop()

    def toggle_color(self, row, col):
        current_color = self.grid_buttons[row][col].cget("bg")
        new_color = "black" if current_color == "white" else "white"
        self.grid_buttons[row][col].config(bg=new_color)

    def grid_component(self):
        for r in range(10):
            row_buttons = []
            for c in range(10):
                btn = tk.Button(self.left_frame, cursor="hand2", bg="white", width=4, height=2, command=lambda r=r, c=c: self.toggle_color(r, c))
                btn.grid(row=r, column=c, padx=1, pady=1)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)

    def buttons_component(self):
        self.save_btn = tk.Button(self.right_frame, text="Save patten", command=self.save_pattern)
        self.save_btn.pack(pady=10)

        self.show_saved_btn = tk.Button(self.right_frame, text="Show saved", command=self.show_saved_patterns)
        self.show_saved_btn.pack(pady=10)

        self.clear_btn = tk.Button(self.right_frame, text="Clear", command=self.clear_grid)
        self.clear_btn.pack(pady=10)

        self.sync_repair_btn = tk.Button(self.right_frame, text="Sync repair", command=self.sync_repair)
        self.sync_repair_btn.pack(pady=10)

        self.async_repair_btn = tk.Button(self.right_frame, text="Async repair", command=self.async_repair)
        self.async_repair_btn.pack(pady=10)

    def save_pattern(self):
        pass

    def show_saved_patterns(self):
        pass

    def clear_grid(self):
        pass

    def sync_repair(self):
        pass

    def async_repair(self):
        pass