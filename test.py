import numpy
import os

a = numpy.zeros((2, 2), dtype = 'i, str')

b = os.get_terminal_size()

print(type(b.columns))