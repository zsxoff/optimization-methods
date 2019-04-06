from collections import namedtuple

Dot = namedtuple('Dot', ['x', 'y', 'color'])
VectorXY = namedtuple('Vector', ['X', 'Y', 'color', 'label'])
LineXH = namedtuple('Line', ['y', 'color'])
LineXV = namedtuple('Line', ['x', 'color'])
