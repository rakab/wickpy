from wickpy import graph

g = graph.Graph()
g.add_node('a')
g.add_node('b')
g.add_node('b')
g.add_node('c')
g.add_node('d')

g.add_edge(('a','b'))
g.add_edge(('b','c'))
g.add_edge(('c','a'))
g.add_edge(('a','d'))

#g.draw_nodes()
