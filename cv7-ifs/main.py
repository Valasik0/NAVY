from models import *
from IFS import IFS

starting_point = [0, 0, 0]
IFS_first = IFS(1000, first_model, starting_point)
IFS_first.transform()
IFS_first.vizualize()

IFS_second = IFS(1000, second_model, starting_point)
IFS_second.transform()
IFS_second.vizualize()
