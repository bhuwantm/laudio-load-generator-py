import os
import pathlib

CURRENT_LOCATION = pathlib.Path(__file__).parent.resolve()
OUTPUT_LOCATION = os.path.join(CURRENT_LOCATION, '..', 'output')
GLOBAL_INITIAL_ID = 5000
