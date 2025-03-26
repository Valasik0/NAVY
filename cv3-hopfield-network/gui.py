import tkinter as tk
from gui_manager import GUIManager

class GUI:
    def __init__(self):
        self.components = []
        self.root = tk.Tk()
        self.root.title("Hopfield network")
        self.root.geometry("550x450")
        self.grid_buttons = []
        self.save_btn = None
        self.show_saved_btn = None
        self.clear_btn = None
        self.sync_repair_btn = None
        self.async_repair_btn = None
        self.left_frame = None
        self.right_frame = None
        self.next_btn = None
        self.prev_btn = None
        self.close_btn = None
        self.choose_pattern_btn = None
        self.gui_manager = GUIManager(grid_buttons=self.grid_buttons)
        

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
        self.save_btn = tk.Button(self.right_frame, text="Save patten", command=self.gui_manager.save_pattern)
        self.save_btn.pack(pady=10)

        self.show_saved_btn = tk.Button(self.right_frame, text="Show saved", command=self.show_saved_patterns)
        self.show_saved_btn.pack(pady=10)

        self.clear_btn = tk.Button(self.right_frame, text="Clear", command=self.gui_manager.clear_grid)
        self.clear_btn.pack(pady=10)

        self.sync_repair_btn = tk.Button(self.right_frame, text="Sync repair", command=self.gui_manager.sync_repair)
        self.sync_repair_btn.pack(pady=10)

        self.async_repair_btn = tk.Button(self.right_frame, text="Async repair", command=self.gui_manager.async_repair)
        self.async_repair_btn.pack(pady=10)

    def show_saved_patterns(self):
        self.save_btn.config(state=tk.DISABLED)
        self.show_saved_btn.config(state=tk.DISABLED)
        self.clear_btn.config(state=tk.DISABLED)
        self.sync_repair_btn.config(state=tk.DISABLED)
        self.async_repair_btn.config(state=tk.DISABLED)
        self.gui_manager.clear_grid()

        
        tmp_frame = tk.Frame(self.right_frame)
        tmp_frame.pack(pady=10)
        self.next_btn = tk.Button(tmp_frame, text="Next ->", command=self.gui_manager.next_pattern)
        self.next_btn.pack(pady=10, side=tk.RIGHT)

        self.prev_btn = tk.Button(tmp_frame, text="<- Prev", command=self.gui_manager.prev_pattern)
        self.prev_btn.pack(pady=10, padx=5, side=tk.LEFT)

        self.choose_pattern_btn = tk.Button(self.right_frame, text="Choose", command=self.gui_manager.choose_pattern)
        self.choose_pattern_btn.pack(pady=10)

        self.close_btn = tk.Button(self.right_frame, text="Close", command=self.close_saved_patterns)
        self.close_btn.pack(pady=10)


    def close_saved_patterns(self):
        self.save_btn.config(state=tk.NORMAL)
        self.show_saved_btn.config(state=tk.NORMAL)
        self.clear_btn.config(state=tk.NORMAL)
        self.sync_repair_btn.config(state=tk.NORMAL)
        self.async_repair_btn.config(state=tk.NORMAL)

        self.right_frame.destroy()
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        self.buttons_component()