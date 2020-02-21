import cv2
import numpy as np
import sympy as sp
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image

class String2Graph(object):
    def __init__(self, expr):
        self.expr = expr

    @property
    def string(self):
        return self.__expr

    @expr.setter
    def expr(self, expr):
        if not isinstance(expr, str):
            raise TypeError("expr should be of type str")
        else:
            self.__expr = expr
