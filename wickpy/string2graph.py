import cv2
import re
import numpy as np
import sympy as sp
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image

from . import Graph

__all__ = [
        'String2Graph',
        ]

class String2Graph(object):
    def __init__(self, expr):
        self.g = Graph()
        self.expr = expr
        matches = set(re.findall(r"(v\d+)\.(v\d+)(\^\d+)?",expr))
        for m in matches:
            self.g.add_node(m[0])
            self.g.add_node(m[1])
            mult = 1
            if m[2] != '':
                mult = int(m[2][1:])
            for i in range(mult):
                self.g.add_edge((m[0],m[1]))


    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr):
        if not isinstance(expr, str):
            raise TypeError("expr should be of type str")
        else:
            self.__expr = expr
