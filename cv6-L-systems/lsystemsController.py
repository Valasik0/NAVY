import math
from LSystem import LSystem


class LSystemsController:
    def __init__(self):
        self.lsystem = None

    def clear_canvas(self, canvas):
        canvas.delete("all")

    def parse_rule(self, rule_text):
        if isinstance(rule_text, str) and '->' in rule_text:
            parts = rule_text.split('->')
            if len(parts) == 2:
                return {parts[0].strip(): parts[1].strip()}
        elif hasattr(rule_text, 'rules'):
            return rule_text.rules
        return {}

    def draw_l_system(self, canvas, l_system_string: str, angle: float, start_x: float, start_y: float, 
                     length: float, start_angle: float = 0, radians: bool = False):
        x, y = start_x, start_y
        current_angle = start_angle
        stack = []  #zasobnik s tuple (x, y, current_angle)
        
        for command in l_system_string:
            if command == 'F': #pohyb s kreslenim
                if radians:
                    rad_angle = current_angle
                else:
                    rad_angle = math.radians(current_angle)
                new_x = x + length * math.cos(rad_angle)
                new_y = y + length * math.sin(rad_angle)
                canvas.create_line(x, y, new_x, new_y, fill="black", width=1)
                x, y = new_x, new_y
            elif command == 'b':  #prohyb bez kresleni
                if radians:
                    rad_angle = current_angle
                else:
                    rad_angle = math.radians(current_angle)
                x += length * math.cos(rad_angle)
                y += length * math.sin(rad_angle)
            elif command == '+':  #otoceni doprava
                current_angle += angle
            elif command == '-':  #otoceni doleva
                current_angle -= angle
            elif command == '[':  #ulozeni pozice a uhlu
                stack.append((x, y, current_angle))
            elif command == ']':  #obnoveni pozice a uhlu
                x, y, current_angle = stack.pop()


    def draw_custom(self, axiom: str, rule_text: str, angle_text: str, canvas, 
                   start_x: float = 50, start_y: float = 50, length: float = 5, 
                   iterations: int = 3, start_angle: float = 0, radians: bool = False):

        angle = float(angle_text)
        
        rules = self.parse_rule(rule_text)
        
        self.lsystem = LSystem(axiom, rules, angle)
        l_system_string = self.lsystem.generate(iterations)

        self.clear_canvas(canvas)

        self.draw_l_system(canvas, l_system_string, angle, start_x, start_y, length, start_angle, radians)
    
    def draw_preset(self, canvas, l_system: LSystem, start_x: float = 50, start_y: float = 50, 
                    length: float = 5, iterations: int = 3, start_angle: float = 0, radians: bool = False):
        self.lsystem = l_system
        l_system_string = self.lsystem.generate(iterations)

        self.clear_canvas(canvas)

        self.draw_l_system(canvas, l_system_string, l_system.angle, start_x, start_y, length, start_angle, radians)