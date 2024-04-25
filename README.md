Network-Theory-Project-2
 Dijkstra's Algorithm or Bellman Ford Algorithm
The inputs are displayed in “network.txt” file containing the graph data. This code opens the specified file and reads all lines. 
The first line indicates the number of nodes, although this value is read, it's not used further in the function. Furthermore, then it initializes a dictionary where each node has another dictionary containing its adjacent nodes and the corresponding edge weights. 
It iterates through the remaining lines, updating the graph dictionary for both directions of each edge since it's an undirected graph. 
With the method we're using Bellman-Fords Algorithm it finds the shortest paths from a single source to all the other nodes in this code and can also handle negative weight edges unlike Dijkstra's algorithm. 
The code runs for |V|-1 iterations, where |V| is the number of vertices in the graph. This ensures that the shortest paths are found if they exist

We both did the same amount of work as we set up a days to meet up and work on it together.