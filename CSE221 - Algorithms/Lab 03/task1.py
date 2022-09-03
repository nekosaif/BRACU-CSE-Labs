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
                
    
    #for debugging purposes            
    def print_edges(self):
        for key in sorted(self.__graph.keys()):
            print(key, end='\t')
            for v in self.__graph[key]:
                print(v, end='\t')
            print()


def tester():
    g = Graph(input_type="file", filename="input.txt")
    #g.print_edges()


def main():
    tester()


if __name__ == '__main__':
    main()