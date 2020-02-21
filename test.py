from wickpy import graph

g = graph.Graph()
g.add_node('a')
g.add_node('b')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')

g.add_edge(('a','b'))
g.add_edge(('b','c'))
g.add_edge(('b','d'))
g.add_edge(('b','d'))
g.add_edge(('d','e'))
g.add_edge(('d','e'))
g.add_edge(('d','e'))
g.add_edge(('d','e'))

g.draw_nodes()
g.draw_edges()
g.draw_img()
