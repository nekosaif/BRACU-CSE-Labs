import heapq
from dataclasses import dataclass, field
from typing import Any
import sys


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
class MinHeapPriorityQueue:
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
        heapq.heappush(self.Queue, PrioritizedItem(priority, item))
        
    def dequeue(self):
        return heapq.heappop(self.Queue).item
    
    def __bool__(self):
        return len(self.Queue) == 0
    
    #for debugging purposes
    def __str__(self):
        return f'{[(PItem.item, PItem.priority) for PItem in self.Queue]}'


class Graph:
    def __init__(self, num_of_vertices, edges):
        self.__graph = {}
        self.__vertices = [str(i+1) for i in range(num_of_vertices)]
        self.__graph = dict.fromkeys(self.__vertices, [])
        self.__num_of_vertices = num_of_vertices
        for u, v, w in edges:
            self.__graph[u] = self.__graph[u] + [(v, int(w))]
            self.__graph[v] = self.__graph[v] + [(u, int(w))]
                      
    def dijkstra(self, source = '1'):
        dist = dict.fromkeys(self.__vertices, float('inf'))
        dist[source] = 0
        Q = MinHeapPriorityQueue((self.__vertices, list(dist.values())))
        visited = dict.fromkeys(self.__vertices, False)
        prev = dict.fromkeys(self.__vertices, None)
        while not Q:
            u = Q.dequeue()
            if visited[u]:
                continue
            visited[u] = True
            for v, w in self.__graph[u]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    Q.enqueue(v, dist[v])
        return dist, prev  
    
    def min_titans_path(self, curr = None, dist = None, prev = None):
        if curr == None and dist == None and prev == None:
            curr = self.__vertices[-1]
            dist, prev = self.dijkstra()
        if curr == '1':
            return ['1']
        return self.min_titans_path(prev[curr], dist, prev) + [curr]
    
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
                graphs.append(Graph(N, edges))
        return graphs              
    
    #for debugging purposes
    def __str__(self):
        ret_str = ''
        for vertex in self.__graph:
            ret_str += f'{vertex}\t->\t{self.__graph[vertex]}\n'
        return ret_str.strip('\n')
            

def tester():
    graphs = Graph.parse_graphs_from_file('input2.txt')
    sys.stdout = open('output2.txt', 'w')
    for graph in graphs:
        print(' '.join(graph.min_titans_path()))


def main():
    tester()


if __name__ == '__main__':
    main()