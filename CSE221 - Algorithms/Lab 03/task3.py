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
    
    
    def DFS_VISIT(self, vertex, endPoint, visited, printed):
        if endPoint in printed:
            return
        visited[int(vertex)-1] = 1
        printed.append(vertex)
        for neighbor in self.__graph[vertex]:
            if visited[int(neighbor)-1] != 1:
                self.DFS_VISIT(neighbor, endPoint, visited, printed)
    
    
    def DFS(self, endPoint, visited = None, printed = None):
        if visited == None:
            visited = [0]*self.__num_of_nodes
            printed = []
        
        for neighbor in list(self.__graph.keys()):
            if endPoint in printed:
                break
            if visited[int(neighbor)-1] != 1:
                self.DFS_VISIT(neighbor, endPoint, visited, printed)
        print('Places: ' + ' '.join(printed))
        

def tester():
    g = Graph(input_type="file", filename="input.txt")
    g.DFS('12')


def main():
    tester()


if __name__ == '__main__':
    main()