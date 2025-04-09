class LSystem:
    def __init__(self, axiom: str, rules: dict, angle: int):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.current_string = axiom