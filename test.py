from wickpy import graph
from wickpy import String2Graph

s = String2Graph('36*v1.v3*v4.v3*v2.v2^2*v3.v3')
s.g.draw_nodes()
s.g.draw_edges()
s.g.draw_img()

#g = graph.Graph()
#g.add_node('a')
#g.add_node('b')
#g.add_node('b')
#g.add_node('c')
#g.add_node('d')
#g.add_node('e')
#
#g.add_edge(('a','b'))
#g.add_edge(('b','c'))
#g.add_edge(('b','d'))
#g.add_edge(('b','d'))
#g.add_edge(('d','e'))
#g.add_edge(('d','e'))
#g.add_edge(('d','e'))
#g.add_edge(('d','e'))
#
#g.draw_nodes()
#g.draw_edges()
#g.draw_img()
