import numpy as np 
import matplotlib.pyplot as plt 
from structs import *

class Box:
    def __init__(self, values):
        self.values = np.array(values)
        self.size = self.values.shape[0]
        self.dig = build_digraph(self.values)
        
    def get_digraph(self):
        return self.dig  
    
    def draw_grid(self):
        size = self.size
        _, ax = plt.subplots(1, 1, figsize=[size]*2)
        ticks = [i for i in range(self.size+1)]
        
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.grid(True)
        ax.tick_params(bottom=False,
                       labelbottom=False,
                       left=False,
                       labelleft=False)
        ax.set_xlim([0, size])
        ax.set_ylim([0, size])

    def plot_weights(self):
        ax = plt.gca()
        size = self.size
        for i in range(size):
            for j in range(size):
                ax.annotate(text=f"{self.values[i, j]}",
                            xy=trans_idx(i, j, 0.4, 0.4, size))

    def get_shortest(self, start: Node, end: Node):
        shortest = shortest_path(self.dig, start, end)
        return shortest
    
    def plot_path(self, path):
        trans = lambda pos: trans_idx(*pos, 0.5, 0.5, self.size)
        
        x, y = zip(*map(trans, path.get_path()))
        ax = plt.gca()
        ax.plot(x, y, 'b')
        ax.scatter(x, y, s=60, color='r')
        
    
    
def trans_idx(i, j, xshift=0, yshift=0, size=3):
    return j + xshift, size - i - yshift
            

def find_paths(graph: Digraph, start: Node, end: Node, path: Path, paths):
    path = path.add_node(start)
    if start == end:
        paths.append(path)
        return paths
    
    for node in graph.children_of(start):
        find_paths(graph, node, end, path, paths)
        
    return paths
        
def shortest_path(graph, start, end):
    paths = find_paths(graph, start, end, Path(), [])
    minimum = paths[0]
    for path in paths:
        print('cost:', path.get_cost(), 'path:', path.get_path())
        if path.get_cost() < minimum.get_cost():
            minimum = path
            
    return minimum
    

def build_digraph(arr):
    dig = Digraph()
    size = len(arr)
    
    for i in range(size):
        for j in range(size):
            dig.add_node(Node(arr[i, j], (i, j)))
    
    for i in range(size):
        for j in range(size):
            src = dig.get_node((i, j))
            down_dig = i+1, j+1
            if down_dig[0] < size and down_dig[1] < size:
                dest = dig.get_node(down_dig)
                dig.add_edge(Edge(src, dest))
            if down_dig[0] < size:
                right = down_dig[0], j
                dest = dig.get_node(right)
                dig.add_edge(Edge(src, dest))
            if down_dig[1] < size:
                left = i, down_dig[1]
                dest = dig.get_node(left)
                dig.add_edge(Edge(src, dest))
    
    return dig
                
    
    

def main():
    BOX = np.random.randint(1, 4, size=[3, 3])

    box = Box(BOX)

    box.draw_grid()
    box.plot_weights()
    dig = box.get_digraph()
    
    start = dig.get_node((0, 0))
    end = dig.get_node((box.size-1,) * 2)
    
    shortest = box.get_shortest(start, end)
    box.plot_path(shortest)
    
    plt.title(f'the shortest path: {shortest.get_cost()}')
    plt.show()

if __name__ == '__main__':
    main()