class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict

    def get_vertexes(self):
        return list(self.gdict.keys())

    def get_edges(self):
        edges = []
        for vertex in self.gdict:
            for adj_vertice in self.gdict[vertex]:
                if {adj_vertice, vertex} not in edges:
                    edges.append({vertex, adj_vertice})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]



