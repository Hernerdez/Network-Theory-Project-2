import heapq

def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    graph = {}
    for line in lines[1:]:
        start, end, weight = line.strip().split()
        weight = float(weight)
        
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
            
        graph[start][end] = weight
        graph[end][start] = weight
    
    return graph

def dijkstra(graph, start):
    shortest_paths = {node: float('infinity') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > shortest_paths[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

filename = input("Please enter the path to the network file: ")
graph = read_graph(filename)
start_node = '0'
shortest_paths = dijkstra(graph, start_node)
print("Shortest paths from node", start_node, ":", shortest_paths)
