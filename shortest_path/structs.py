class Node:
    def __init__(self, weight: int, position: tuple):
        self.weight = weight
        self.position = position
        
    def get_weight(self) -> int:
        return self.weight
    
    def get_position(self) -> tuple:
        return self.position
    

class Edge:
    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest 
    
    def get_src(self) -> Node:
        return self.src 
    
    def get_dest(self) -> Node:
        return self.dest 
    
    def __str__(self) -> str:
        return f"{self.src.get_position()} -> {self.dest.get_position()}"
    
    
class Digraph:
    def __init__(self):
        self.edges = {}
        
    def get_edges(self):
        return self.edges
        
    def add_node(self, node: Node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    
    def add_edge(self, edge: Edge):
        src = edge.get_src()
        dest = edge.get_dest()
        
        if src not in self.edges:
            self.edges[src] = []
        if dest not in self.edges:
            self.edges[dest] = []
            
        self.edges[src].append(dest)
    
    def get_node(self, position: tuple) -> Node:
        for n in self.edges:
            if n.get_position() == position:
                return n
        raise NameError(f"{position} not in the graph")
    
    def children_of(self, node: Node) -> list[Node]:
        return self.edges[node]
    
    def has_node(self, node: Node) -> bool:
        return node in self.edges
    
    def __str__(self) -> str:
        result = ''
        
        for src in self.edges:
            for dest in self.edges[src]:
                result += f"{src.get_position()} ->\
                            {dest.get_position()}\n"
                            
        return result[:-1]       


class Path:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.cost, self.path = self.__calculations()
    
    def __calculations(self):
        nodes = self.nodes
        cost, path = 0, []

        for n in nodes:
            cost += n.get_weight()
            path.append(n.get_position())
            
        return cost, path
    
    def get_nodes(self) -> list[Node]:
        """ Returns list of nodes in the path """
        return self.nodes
    
    def get_cost(self) -> int:
        """ Returns the total sum of the weights of the path """
        return self.cost
    
    def get_path(self) -> list[tuple]:
        """ Returns list of tuples that represents the positions of the nodes """
        return self.path
    
    def add_node(self, node: Node):
        """ Adds a new node at the end of the path """
        self.nodes.append(node)
        self.cost += node.get_weight()
        self.path.append(node.get_position())
    
    def has(self, node: Node):
        return node in self.nodes

    