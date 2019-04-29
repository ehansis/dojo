import networkx as nx


class Dep:

    def __init__(self):
        self.G = nx.DiGraph()

    def add(self, node, targets):
        # existing edges and nodes are quietly ignored, non-existent nodes are created
        self.G.add_edges_from((node, t) for t in targets)

    def deps(self, node):
        # dfs returns source node in result set, remove it
        return set(nx.dfs_preorder_nodes(self.G, source=node)) - {node}
