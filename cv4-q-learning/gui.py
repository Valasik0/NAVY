import tkinter as tk
from q_manager import QLearningManager
import numpy as np
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.components = []
        self.root = tk.Tk()
        self.root.title("Mouse cheese game")
        self.root.geometry("700x500")
        self.grid_buttons = []
        self.left_frame = None
        self.right_frame = None
        self.mouse_position = None
        self.cheese_position = None
        self.walls = []
        self.traps = []
        
        self.start_learning_btn = None
        self.find_cheese_btn = None
        self.select_mouse_btn = None
        self.select_trap_btn = None
        self.select_wall_btn = None
        self.select_cheese_btn = None
        self.show_values_btn = None
        self.show_memory_btn = None
        self.clear_grid_btn = None
        
        self.selection_mode = None

        self.mouse_img = tk.PhotoImage(file="assets\\mouse.png")
        self.wall_img = tk.PhotoImage(file="assets\\wall.png")
        self.cheese_img = tk.PhotoImage(file="assets\\cheese.png")
        self.trap_img = tk.PhotoImage(file="assets\\trap.png")
        self.empty_img = tk.PhotoImage(file="assets\\empty.png")
        

        self.q_manager = QLearningManager(10, 10)  # 10x10 grid

    def run(self):
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.grid_component()
        self.buttons_component()

        self.root.mainloop()

    def toggle_cell(self, row, col):
        if self.selection_mode == "mouse":
            if self.mouse_position:
                old_row, old_col = self.mouse_position
                self.grid_buttons[old_row][old_col].config(image=self.empty_img)
            
            self.mouse_position = (row, col)
            self.grid_buttons[row][col].config(image=self.mouse_img)
            
        elif self.selection_mode == "cheese":
            if self.cheese_position:
                old_row, old_col = self.cheese_position
                self.grid_buttons[old_row][old_col].config(image=self.empty_img)
            
            self.cheese_position = (row, col)
            self.grid_buttons[row][col].config(image=self.cheese_img)
            
        elif self.selection_mode == "wall":
            current_image = self.grid_buttons[row][col].cget("image")
            if current_image == str(self.wall_img):
                self.grid_buttons[row][col].config(image=self.empty_img)
                self.walls.remove((row, col))
            else:
                self.grid_buttons[row][col].config(image=self.wall_img)
                self.walls.append((row, col))
                
        elif self.selection_mode == "trap":
            current_image = self.grid_buttons[row][col].cget("image")
            if current_image == str(self.trap_img):
                self.grid_buttons[row][col].config(image=self.empty_img)
                self.traps.remove((row, col))
            else:
                self.grid_buttons[row][col].config(image=self.trap_img)
                self.traps.append((row, col))

    def grid_component(self):
        for r in range(10):
            row_buttons = []
            for c in range(10):
                btn = tk.Button(self.left_frame, image=self.empty_img, relief='flat', cursor="hand2", bg="white", width=40, height=40, 
                               command=lambda r=r, c=c: self.toggle_cell(r, c))
                btn.grid(row=r, column=c, padx=1, pady=1)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)

    def buttons_component(self):

        self.select_mouse_btn = tk.Button(self.right_frame, text="Select a mouse", bg="lightblue",
                                         command=lambda: self.set_selection_mode("mouse"))
        self.select_mouse_btn.pack(pady=5, fill=tk.X)
        
        self.select_cheese_btn = tk.Button(self.right_frame, text="Select a cheese", bg="lightblue",
                                          command=lambda: self.set_selection_mode("cheese"))
        self.select_cheese_btn.pack(pady=5, fill=tk.X)
        
        self.select_trap_btn = tk.Button(self.right_frame, text="Select a trap", bg="lightblue",
                                        command=lambda: self.set_selection_mode("trap"))
        self.select_trap_btn.pack(pady=5, fill=tk.X)
        
        self.select_wall_btn = tk.Button(self.right_frame, text="Select a wall", bg="lightblue",
                                        command=lambda: self.set_selection_mode("wall"))
        self.select_wall_btn.pack(pady=5, fill=tk.X)
        
        # Tlačítka pro akce
        self.start_learning_btn = tk.Button(self.right_frame, text="Start learning", bg="lightgreen",
                                           command=self.start_learning)
        self.start_learning_btn.pack(pady=5, fill=tk.X)
        
        self.find_cheese_btn = tk.Button(self.right_frame, text="Let's find the cheese!", bg="lightgreen",
                                        command=self.find_cheese)
        self.find_cheese_btn.pack(pady=5, fill=tk.X)
        
        self.show_values_btn = tk.Button(self.right_frame, text="Show values of matrix", bg="lightblue",
                                        command=self.show_q_values)
        self.show_values_btn.pack(pady=5, fill=tk.X)
        
        self.show_memory_btn = tk.Button(self.right_frame, text="Show values of memory matrix", bg="lightblue",
                                        command=self.show_memory_matrix)
        self.show_memory_btn.pack(pady=5, fill=tk.X)
        
        self.clear_grid_btn = tk.Button(self.right_frame, text="Clear grid", bg="pink",
                                       command=self.clear_grid)
        self.clear_grid_btn.pack(pady=5, fill=tk.X)
        
        info_label = tk.Label(self.right_frame, text="Only one mouse can be placed")
        info_label.pack(pady=10)

    def set_selection_mode(self, mode):
        self.selection_mode = mode
        
        buttons = {
            "mouse": self.select_mouse_btn,
            "cheese": self.select_cheese_btn,
            "trap": self.select_trap_btn,
            "wall": self.select_wall_btn
        }
        
        for btn_mode, btn in buttons.items():
            if btn_mode == mode:
                btn.config(bg="yellow")
            else:
                btn.config(bg="lightblue")

    def start_learning(self):
        if not self.mouse_position or not self.cheese_position:
            tk.messagebox.showinfo("Error", "Place both mouse and cheese first")
            return
        self.q_manager.set_environment(self.mouse_position, self.cheese_position, self.walls, self.traps)
        episodes = self.q_manager.train()
        tk.messagebox.showinfo("Training Complete", f"Training completed in {episodes} episodes")

    def find_cheese(self):
        if not self.mouse_position or not self.cheese_position:
            tk.messagebox.showinfo("Error", "Place both mouse and cheese first")
            return
        path = self.q_manager.find_path(self.mouse_position, self.cheese_position)
        self.animate_path(path)

    def animate_path(self, path):
        if not path:
            messagebox.showinfo("Error", "No path found")
            return
        
        print("Nalezená cesta:", path)  # Přidejte pro ladění
        
        # Resetujeme původní pozici myši
        old_row, old_col = self.mouse_position
        self.grid_buttons[old_row][old_col].config(image=self.empty_img)
        
        animation_path = path.copy()
        
        def move_mouse(index):
            if index >= len(animation_path):
                # Na konci cesty zobrazíme myš na sýru
                row, col = animation_path[-1]
                self.grid_buttons[row][col].config(image=self.mouse_img)
                return
            
            # Aktuální pozice
            row, col = animation_path[index]
            
            # Zobrazíme myš na aktuální pozici
            self.grid_buttons[row][col].config(image=self.mouse_img)
            
            # Označíme předchozí pozici jako součást cesty
            if index > 0:
                prev_row, prev_col = animation_path[index-1]
                self.grid_buttons[prev_row][prev_col].config(image=self.empty_img)
                self.grid_buttons[prev_row][prev_col].config(bg="lightblue")
            
            # Naplánujeme další krok
            self.root.after(500, lambda: move_mouse(index+1))
        
        # Spustíme animaci
        move_mouse(0)

    def show_q_values(self):
        if not hasattr(self.q_manager, 'q_table'):
            tk.messagebox.showinfo("Error", "Q-matrix not initialized. Start learning first.")
            return
            
        print("=== Q-VALUES MATRIX ===")
        print(self.q_manager.q_table)

    def show_memory_matrix(self):
        if not hasattr(self.q_manager, 'visits'):
            tk.messagebox.showinfo("Error", "Memory matrix not initialized. Start learning first.")
            return
            
        print("=== MEMORY MATRIX ===")
        print(self.q_manager.visits)

    def clear_grid(self):
        for row in self.grid_buttons:
            for btn in row:
                btn.config(bg="white")
                btn.config(image=self.empty_img)
        self.mouse_position = None
        self.cheese_position = None
        self.walls = []
        self.traps = []
