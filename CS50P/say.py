#Using the function from sayings.py

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])