import printing_functions
from printing_functions import print_models
from printing_functions import show_completed_models as show
import printing_functions as mn
from printing_functions import *


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show(completed_models)
