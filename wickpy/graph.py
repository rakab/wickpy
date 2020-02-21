import cv2
import numpy as np
import sympy as sp
from io import BytesIO
from PIL import ImageFont, ImageDraw, Image

from . import draw_arc, draw_bubble

__all__ = [
        'Graph',
        'Node',
        ]

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
        if name not in [n.name for n in self.nodes]:
            self.nodes.append(Node(name))

    def add_edge(self, edge):
        if self[edge[0]] is not None and self[edge[1]] is not None:
            self[edge[0]].add_edge(edge[1])
            if self[edge[0]] != self[edge[1]]:
                self[edge[1]].add_edge(edge[0])

    def assign_xy(self):
        for i,n in enumerate(self.nodes):
            n.xy = (50+50*i,200)

    def draw_nodes(self):
        self.assign_xy()
        for n in self.nodes:
            cv2.circle(self.img, n.xy, 5, (0,0,0), -1)

    def draw_edges(self):
        for n in self.nodes:
            for e in n.edges:
                print(n.name," ",e)
                mult = n.edges[e]
                if mult>1:
                    sagitta = [-100+i*200/(mult-1) for i in range(mult)]
                else:
                    n_between = 0 #number of nodes between two connected node
                    for nx in self.nodes:
                        if min(n.xy[0],self[e].xy[0])<nx.xy[0]<max(n.xy[0],self[e].xy[0]):
                            n_between += 1
                    if not n_between:
                        sagitta = [0]
                    else:
                        sagitta = [100]
                for i in range(mult): #edge multiplicity
                    if n.name == e:
                        draw_bubble(self.img,n.xy,i*2*np.pi/mult)
                    else:
                        draw_arc(self.img,n.xy,self[e].xy,sagitta[i],0,0)
                self[e].edges[n.name] = 0

    def draw_img(self):
        cv2.imshow('', self.img)
        cv2.waitKey()

class Node(object):
    def __init__(self, name=''):
        self.name = name
        self.xy = (0,0)
        self.edges = {}

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

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges[edge] = 1
        else:
            self.edges[edge] += 1

    def num_edges(self):
        return len(self.edges)
