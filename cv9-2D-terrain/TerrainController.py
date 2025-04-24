class TerrainController:
    def __init__(self):
        pass

    def draw_terrain(self, start_x, start_y, iterations, line_length, offset_num, color):
        
        
    def validate_numeric_input(self, input_value):
        try:
            value = float(input_value)
            return value
        except ValueError:
            return None