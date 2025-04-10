from models import *
from IFS import IFS

my_IFS = IFS(1000, first_model, (0, 0, 0))
my_IFS.transform()
my_IFS.vizualize()
