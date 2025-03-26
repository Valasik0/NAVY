from tkinter import messagebox
import tkinter as tk
from initial_patterns import initial_patterns
from hopfield_network import HopfieldNetwork
import numpy as np

class GUIManager:
    def __init__(self, grid_buttons):
        self.grid_buttons = grid_buttons
        self.pattern_index = 0
        self.saved_patterns = initial_patterns.copy()
        self.hopfield = HopfieldNetwork(10*10)
        self.hopfield.train(self.saved_patterns)

    

    def clear_grid(self):
        for row in self.grid_buttons:
            for btn in row:
                btn.config(bg="white")



    def save_pattern(self):
        if len(self.saved_patterns) == 5:
            tk.messagebox.showinfo("Info", "You can save only 5 patterns")
            return
        pattern = []
        for btn in self.grid_buttons:
            for b in btn:
                if b.cget("bg") == "black":
                    pattern.append(1)
                else:
                    pattern.append(-1)
        self.saved_patterns.append(pattern)
        self.hopfield.train(self.saved_patterns) 

    def delete_pattern(self):
        if len(self.saved_patterns) == 0:
            tk.messagebox.showinfo("Info", "No patterns to delete")
            return
        
        self.saved_patterns.pop(self.pattern_index)
        self.pattern_index = 0
        self.clear_grid()
        self.hopfield.train(self.saved_patterns)
        if self.saved_patterns:
            self.draw_pattern(self.saved_patterns[0])



    def sync_repair(self):
        pattern = self.get_current_pattern()
        repaired_pattern = self.hopfield.sync_update(pattern)
        self.draw_pattern(repaired_pattern)

    def async_repair(self):
        pattern = self.get_current_pattern()
        repaired_pattern = self.hopfield.async_update(pattern)
        self.draw_pattern(repaired_pattern)

    def get_current_pattern(self):
        return np.array([1 if btn.cget("bg") == "black" else -1 for row in self.grid_buttons for btn in row])


    def next_pattern(self):
        for pattern in self.saved_patterns:
            if self.pattern_index == len(self.saved_patterns) - 1:
                self.pattern_index = 0
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            else:
                self.pattern_index += 1
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            break

    def draw_pattern(self, pattern):
        for i, btn in enumerate(sum(self.grid_buttons, [])):
            btn.config(bg="black" if pattern[i] == 1 else "white")

    def prev_pattern(self):
        for _ in self.saved_patterns:
            if self.pattern_index == 0:
                self.pattern_index = len(self.saved_patterns) - 1
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            else:
                self.pattern_index -= 1
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            break