import numpy as np 
import matplotlib.pyplot as plt 
from structs import *

class Box:
    def __init__(self, values):
        self.values = np.array(values)
        self.size = self.values.shape[0]
    
    def draw_grid(self, size=3):
        _, ax = plt.subplots(1, 1, figsize=[size]*2)
        ticks = [i for i in range(self.size+1)]
        
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.grid(True)
        ax.tick_params(bottom=False,
                       labelbottom=False,
                       left=False,
                       labelleft=False)

    def plot_weights(self):
        ax = plt.gca()
        size = self.size
        for i in range(size):
            for j in range(size):
                ax.annotate(text=f"{self.values[i, j]}",
                            xy=trans_idx(i, j, 0.4, -0.4, size))

def trans_idx(i, j, xshift=0, yshift=0, size=3):
    return j + xshift, size - i + yshift
            
    
def DFS(graph: Digraph, start: Node, end: Node,
        path: Path, shortest: Path) -> Path:  
    """ Assumes graph is a Digraph; start and end are nodes;
        path and shortest are lists of nodes
        Returns a shortest path from start to end in graph """
    path = path.add_node(start)
    
    if start == end:
        return path
    
    for node in graph.children_of(start):
        if not path.has(node): # avoid cycles
            if shortest is None or path.get_cost() < shortest.get_cost():
                new_path = DFS(graph, node, end, path, shortest)
                if new_path is not None:
                    shortest = new_path
                    
    return shortest


def shortest_path(graph: Digraph, start: Node, end: Node) -> Path:
    """ Assumes graph is a Digraph; start and end are nodes
        Returns a shortest path from start to end in graph"""
    return DFS(graph, start, end, Path(), None)

def build_digraph(arr):
    dig = Digraph()
    size = len(arr)
    
    for i in range(size):
        for j in range(size):
            src = Node(arr[i, j], (i, j))
            nxt = i+1, j+1
            if nxt[0] < size and nxt[1] < size:
                dest = Node(arr[*nxt], nxt)
                dig.add_edge(Edge(src, dest))
            if nxt[0] < size:
                nxt = nxt[0], j
                dest = Node(arr[*nxt], nxt)
                dig.add_edge(Edge(src, dest))
            if nxt[1] < size:
                nxt = i, nxt[1]
                dest = Node(arr[*nxt], nxt)
                dig.add_edge(Edge(src, dest))
                
    
    

def main():
    # BOX = [list(map(int, input().split())) for _ in range(3)]
    BOX = [
        [2, 14, 15],
        [16, 29, 13],
        [13, 12, 7]
    ]

    box = Box(BOX)

    box.draw_grid()
    box.plot_weights()

    plt.show()

if __name__ == '__main__':
    main()