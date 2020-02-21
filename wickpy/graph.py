import cv2
import numpy as np
import sympy as sp
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        #self.__nodes = []
        self.nodes = []

        self.img = np.zeros((500, 500), dtype=np.uint8)
        self.img.fill(255)

    #@property
    #def nodes(self):
        #names=[]
        #for n in self.__nodes:
            #names.append(n.name)
        #return names

    def __getitem__(self, name):
        """
        For given parameter name return a corresponding list of the graphs
        """
        for n in self.nodes:
            if name == n.name:
                return n
        else:
            return None

    def __getattr__(self, name):
        return self[name]


    def add_node(self, name):
        if not len(self.nodes):
            self.nodes.append(Node(name))
        for n in self.nodes:
            if name not in n.name:
                self.nodes.append(Node(name))

    def add_edge(self, edge):
        if self[edge[0]] is not None and self[edge[1]] is not None:
            self[edge[0]].add_edge(edge[1])
            self[edge[1]].add_edge(edge[0])

    def draw_nodes(self):
        for i,n in enumerate(self.nodes):
            cv2.circle(self.img, (50+50*i,200), 5, (0,0,0), -1)

    def draw_edges(self):
        for n in self.nodes:
            edges = self.edges_from_node(n)
            for i, e in enumerate(edges):
                cv2.circle(self.img, (50+50*i,200), 5, (0,0,0), -1)

    def draw_img(self):
        cv2.imshow('', img)
        cv2.waitKey()

class Node(object):
    def __init__(self, name=''):
        self.name = name
        self.xy = (0,0)
        self.edges = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name should be of type str")
        else:
            self.__name = name

    @property
    def xy(self):
        return self.__xy

    @xy.setter
    def xy(self, coords):
        if not isinstance(coords, tuple):
            raise TypeError("coordinates should be of type tuple (int, int)")
        else:
            self.__xy = coords

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, edges):
        self.__edges = edges

    def edge_mult(self, edge):
        #for self.edges

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append((edge,0))
        else:
            self.edges[]

    def num_edges(self):
        return len(self.edges)
