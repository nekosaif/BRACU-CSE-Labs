from collections import deque


class Graph:
    def __init__(self, input_data=None, **kwargs):
        if kwargs["input_type"] == "file":
            self.__graph = {}
            self.__parse_graph_from_file(kwargs.get("filename", "input.txt"))


    def __parse_graph_from_file(self, filename, delimiter="\t"):
        with open(filename, "r") as f:
            input_data = f.read().strip().split("\n")
            self.__num_of_nodes = int(input_data[0])
            
            #auto-detect sample inputs type
            if len(input_data) == (self.__num_of_nodes + 1):
                self.__num_of_edges = 0
                for node in input_data[1::]:
                    list_of_edges = node.split(delimiter)
                    if len(list_of_edges) > 1:
                        self.__graph[list_of_edges[0]] = list_of_edges[1::]
                        self.__num_of_edges += len(list_of_edges[1::])
                    else:
                        self.__graph[list_of_edges[0]] = []
            else:
                self.__num_of_edges = int(input_data[1])
                for edge in input_data[2::]:
                    a, b = edge.split(delimiter)
                    self.__graph[a] = self.__graph.get(a, []) + [b]
                    self.__graph[b] = self.__graph.get(b, [])
    
    
    def BFS(self, node, endPoint, visited = None, q = deque()):
        print('Places:', end=' ')
        if visited == None:
            visited = [0]*self.__num_of_nodes
        visited[int(node)-1] = 1
        q.append(node)
        while q:
            m = q.popleft()
            print(m, end=' ')
            if m == endPoint:
                break
            for neighbour_node in self.__graph[m]:
                if visited[int(neighbour_node)-1] == 0:
                    visited[int(neighbour_node)-1] = 1
                    q.append(neighbour_node)


def tester():
    g = Graph(input_type="file", filename="input.txt")
    g.BFS('1', '12')


def main():
    tester()


if __name__ == '__main__':
    main()