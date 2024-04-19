import heapq

def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # The number of nodes (not actually used in building the graph dictionary)
    num_nodes = int(lines[0].strip())
    
    # Initialize the graph as a dictionary of dictionaries
    graph = {}
    for line in lines[1:]:
        start, end, weight = line.strip().split()
        weight = float(weight)
        
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
            
        # As it's an undirected graph, add both pairs
        graph[start][end] = weight
        graph[end][start] = weight
    
    return graph

def dijkstra(graph, start):
    # Dictionary to hold the shortest path from start to each node
    shortest_paths = {node: float('infinity') for node in graph}
    shortest_paths[start] = 0
    
    # Priority queue to hold nodes to explore
    priority_queue = [(0, start)]
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > shortest_paths[current_node]:
            continue

        # Explore each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Read the graph from the file
filename = 'network.txt'
graph = read_graph(filename)

# Define the starting node, for example, node '0'
start_node = '0'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node", start_node, ":", shortest_paths)
