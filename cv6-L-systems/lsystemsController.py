from gui import GUI

class LSystemsController:
    def __init__(self):
        self.gui = GUI()

    
    def run(self):
        self.gui.run()

    def clear_canvas(self):
        self.gui.canvas.delete("all")
    