class GUIManager:
    def __init__(self, grid_buttons):
        self.saved_patterns = []
        self.grid_buttons = grid_buttons
        self.pattern_index = 0

    def clear_grid(self):
        for row in self.grid_buttons:
            for btn in row:
                btn.config(bg="white")



    def save_pattern(self):
        pattern = []
        for btn in self.grid_buttons:
            for b in btn:
                if b.cget("bg") == "black":
                    pattern.append(1)
                else:
                    pattern.append(0)
        self.saved_patterns.append(pattern)
        

    def sync_repair(self):
        pass

    def async_repair(self):
        pass

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
        for i, btn in enumerate(self.grid_buttons):
            for j, b in enumerate(btn):
                if pattern[i * 10 + j] == 1:
                    b.config(bg="black")
                else:
                    b.config(bg="white")

    def prev_pattern(self):
        for _ in self.saved_patterns:
            if self.pattern_index == 0:
                self.pattern_index = len(self.saved_patterns) - 1
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            else:
                self.pattern_index -= 1
                self.draw_pattern(self.saved_patterns[self.pattern_index])
            break

    def choose_pattern(self):
        pass