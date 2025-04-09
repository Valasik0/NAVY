class LSystem:
    def __init__(self, axiom: str, rules: dict, angle: float):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle

    def generate(self, iterations: int) -> str:
        result = self.axiom
        for _ in range(iterations):
            new_result = ""
            for char in result:
                if char in self.rules:
                    new_result += self.rules[char]
                else:
                    new_result += char
            result = new_result
        return result