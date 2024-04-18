class Graph:
    def __init__(self, vertices):
        self.M = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges
        self.predecessor = [-1] * self.M  # Array to store the path

    # Add edges
    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])

    # Function to print the shortest path from the source
    def print_path(self, j):
        if self.predecessor[j] == -1:
            print(j, end='')
            return
        self.print_path(self.predecessor[j])
        print("->{}".format(j), end='')

    # Print the solution
    def print_solution(self, src, distance):
        print("Shortest paths from source node {}:".format(src))
        for i in range(1, self.M):
            print("Shortest path to node {} is ".format(i), end='')
            self.print_path(i)
            print(" with cost {:.1f}".format(distance[i]))

    # Bellman-Ford algorithm
    def bellman_ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0
        self.predecessor[src] = -1  # Source has no predecessor

        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
                    self.predecessor[b] = a

        # Check for negative weight cycles
        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(src, distance)

# Reading the file and processing the graph
def process_file(filename, src):
    try:
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            if not first_line:
                raise ValueError("First line is empty, expected number of vertices.")
            num_vertices = int(first_line)
            graph = Graph(num_vertices)
            for line in file:
                parts = line.split()
                if len(parts) != 3:
                    continue  # Skip any lines that do not have exactly three elements
                a, b, c = parts
                graph.add_edge(int(a), int(b), float(c))
        graph.bellman_ford(src)
    except FileNotFoundError:
        print("File not found: {}".format(filename))
    except ValueError as e:
        print("ValueError: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

# Example usage
process_file('network.txt', 0)