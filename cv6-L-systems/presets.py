from LSystem import LSystem
first = LSystem("F+F+F+F", {"F": "F+F-F-FF+F+F-F"}, "90")
second = LSystem("F++F++F", {"F": "F+F--F+F"}, "60")
third = LSystem("F", {"F": "F[+F]F[-F]F"}, "pi/7")
forth = LSystem("F", {"F": "FF+[+F-F-F]-[-F+F+F]"}, "pi/8")