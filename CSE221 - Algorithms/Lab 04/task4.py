import heapq
from dataclasses import dataclass, field
from typing import Any
import sys


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
class MaxHeapPriorityQueue:
    #data: lst <- [(item_n, priority_n),]
    #data: tuple <- ([item_n,], [priority_n,])
    def __init__(self, data=None):
        self.Queue: [PrioritizedItem] = []
        if isinstance(data, list):
            for item_priority in data:
                self.enqueue(*item_priority)
        elif isinstance(data, tuple):
            items, priorities = data
            for item, priority in zip(items, priorities):
                self.enqueue(item, priority)
    
    def enqueue(self, item, priority: int):
        heapq.heappush(self.Queue, PrioritizedItem(-priority, item))
        
    def dequeue(self):
        return heapq.heappop(self.Queue).item
    
    def __bool__(self):
        return len(self.Queue) == 0
    
    #for debugging purposes
    def __str__(self):
        return f'{[(PItem.item, PItem.priority) for PItem in self.Queue]}'


class Graph:
    def __init__(self, num_of_vertices, edges, **kwargs):
        self.__graph = {}
        self.__vertices = [str(i+1) for i in range(num_of_vertices)]
        self.__source = kwargs.get('source', self.__vertices[0])
        self.__graph = dict.fromkeys(self.__vertices, [])
        self.__num_of_vertices = num_of_vertices
        for u, v, d in edges:
            self.__graph[u] = self.__graph[u] + [(v, int(d))]
                      
    def network(self, source = None):
        source = self.__source if source == None else source
        dist = dict.fromkeys(self.__vertices, float('-inf'))
        dist[source] = float('inf')
        Q = MaxHeapPriorityQueue((self.__vertices, list(dist.values())))
        prev = dict.fromkeys(self.__vertices, None)
        while not Q:
            u = Q.dequeue()
            for v, d in self.__graph[u]:
                alt = min(dist[u], d)
                if alt > dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Q.enqueue(v, dist[v])
        for k in dist:
            dist[k] = 0 if dist[k]==float('inf') else -1 if dist[k]==float('-inf') else dist[k]
        return dist, prev
    
    def max_data_transfer(self):
        return list(self.network()[0].values())
    
    @classmethod
    def parse_graphs_from_file(cls, filename):
        graphs = []
        with open(filename, 'r') as f:
            num_of_graphs = int(f.readline().strip())
            for i in range(num_of_graphs):
                N, M = list(map(int, f.readline().strip().split(' ')))
                edges = []
                for i in range(M):
                    edges.append(f.readline().strip().split(' '))
                source_vertex = f.readline().strip()
                graphs.append(Graph(N, edges, source=source_vertex))
        return graphs
    
    #for debugging purposes
    def __str__(self):
        ret_str = ''
        for vertex in self.__graph:
            ret_str += f'{vertex}\t->\t{self.__graph[vertex]}\n'
        return ret_str.strip('\n')
            

def tester():
    graphs = Graph.parse_graphs_from_file('input4.txt')
    sys.stdout = open('output4.txt', 'w')
    for graph in graphs:
        print(' '.join(map(str, graph.max_data_transfer())))


def main():
    tester()


if __name__ == '__main__':
    main()