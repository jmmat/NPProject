"""
    name: Duy Bui, Tomas Castillo, Justin Martin
    
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

#Program Type:
# This program is a greedy algorithm that aims to color the vertices 
# of an undirected graph using the minimum number of colors such that 
# no two adjacent vertices have the same color.

#Polynomial Time:
# This program runs in polynomial time because it uses a simple greedy algorithm
# that iterates over each vertex and checks its neighbors
# 'colors to assign the lowest available color. The runtime of the program depends 
# on the number of vertices and edges in the input graph, but it has a time complexity of O(|V|^2), 
# where |V| is the number of vertices in the graph. Therefore, the program runs in polynomial time.

# Reasonable Approximation:
# The greedy graph coloring algorithm is a reasonable approximation 
# because it uses a heuristic to find a solution that is close to the optimal solution. 
# In the worst-case scenario, this algorithm may use more colors than the minimum needed to color the graph optimally. 
# However, it usually produces a coloring that uses a small number of colors.

import sys

def is_valid_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if color == coloring[neighbor]:
                return False
    return True

def greedy_graph_coloring(G):
    color = {} # dictionary to store the assigned color of each vertex
    for v in range(len(G)):
        used_colors = set(color[u] for u in G[v+1] if u in color and u != v + 1)
        if not used_colors:
            color[v+1] = 0 # assign the first available color
        else:
            color[v+1] = min(c for c in range(1, len(G)+1) if c not in used_colors) # assign the lowest available color
    return color

def main():
    # Read graph data from file
    if len(sys.argv) < 2:
        print("Usage: python graph_coloring.py input_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        G = {i: set() for i in range(1, n+1)}
        for line in f:
            u, v = map(int, line.split())
            G[u].add(v)
            G[v].add(u)

    # Compute the graph coloring using the Greedy algorithm
    color = greedy_graph_coloring(G)
    
    print(is_valid_coloring(G, color))
    
    # Print the assigned color of each vertex
    print(len(set(color.values())))
    for v in sorted(color, reverse=True):
        print(v, color[v])

if __name__ == "__main__":
    main()
