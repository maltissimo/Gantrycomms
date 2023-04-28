"""
This script interprets what is coming from the
gantry move blablbla command line as issued by the user on the shell,
and translates it via sys.argv into something that PMAC can understand

The syntax for the command is

gantry COMMAND TYPE NUMBER

the python code takes care of direction.
so
sys.argv[0] = gantry
sys.argv[1] = move
sys.argv[2] = rel or abs
sys.argv[3] = distance/coordinate

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""


import sys
