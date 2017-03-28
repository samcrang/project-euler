class Edge:
    def __init__(self, source, destination, weight):
        self.destination = destination
        self.source = source
        self.weight = weight

class Vertex:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def get_vertex(self, name):
        for v in self.vertices:
            if v.name == name:
                return v

"""
https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
"""
def bellman_ford(graph, start, target):
    distance = {}
    predecessor = {}

    for v in graph.vertices:
        distance[v.name] = float("inf")
        predecessor[v.name] = None

    distance[start.name] = 0

    for v in graph.vertices:
        for e in graph.edges:
            if distance[e.source.name] + e.weight < distance[e.destination.name]:
                distance[e.destination.name] = distance[e.source.name] + e.weight
                predecessor[e.destination.name] = e.source.name

    return distance[target.name]

def tree_to_graph(tree):
    g = Graph()

    start = Vertex("start")
    end = Vertex("end")
    g.add_vertex(start)
    g.add_vertex(end)
    for r_idx, row in enumerate(tree):
        for c_idx, column in enumerate(row):
            if r_idx == 0:
                v = Vertex("{},{}".format(r_idx, c_idx))
                g.add_vertex(v)
                g.add_edge(start, v, column * -1)
            else:
                v = Vertex("{},{}".format(r_idx, c_idx))
                g.add_vertex(v)
                if c_idx == 0:
                    parent = g.get_vertex("{},{}".format(r_idx-1, 0))
                    g.add_edge(parent, v, column *- 1)
                elif c_idx == len(row) - 1:
                    parent = g.get_vertex("{},{}".format(r_idx-1, c_idx - 1))
                    g.add_edge(parent, v, column * -1)
                else:
                    parent = g.get_vertex("{},{}".format(r_idx-1, c_idx))
                    g.add_edge(parent, v, column * -1)

                    parent = g.get_vertex("{},{}".format(r_idx-1, c_idx-1))
                    g.add_edge(parent, v, column * -1)

                if r_idx == len(tree) - 1:
                    g.add_edge(v, end, 0)

    return g

def answer(tree):
    g = tree_to_graph(tree)
    return bellman_ford(g, g.get_vertex("start"), g.get_vertex("end")) * -1

def solution():
    return answer([\
        [75], \
        [95,64], \
        [17,47,82], \
        [18,35,87,10], \
        [20,4,82,47,65], \
        [19,1,23,75,3,34], \
        [88,2,77,73,7,63,67], \
        [99,65,4,28,6,16,70,92], \
        [41,41,26,56,83,40,80,70,33], \
        [41,48,72,33,47,32,37,16,94,29], \
        [53,71,44,65,25,43,91,52,97,51,14], \
        [70,11,33,28,77,73,17,78,39,68,17,57], \
        [91,71,52,38,17,14,91,43,58,50,27,29,48], \
        [63,66,4,68,89,53,67,30,73,16,69,87,40,31], \
        [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23] \
    ])
