"""
    name: Duy Bui, Tomas Castillo, Justin Martin
    
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

import sys

def greedy_graph_coloring(G):
    color = {} # dictionary to store the assigned color of each vertex
    for v in range(len(G)):
        # Correct the used_colors set construction
        used_colors = set(color[u] for u in G[v+1] if u in color)
        if not used_colors:
            color[v+1] = 1 # assign the first available color
        else:
            color[v+1] = min(c for c in range(1, len(G)+1) if c not in used_colors) # assign the lowest available color
    return color

def main():
    # Read graph data from file
    with open('cs412/final/color_graph_test.txt', 'r') as f:
        n = int(f.readline().strip())
        G = {i: set() for i in range(1, n+1)}
        for line in f:
            u, v = map(int, line.split())
            G[u].add(v)
            G[v].add(u)

    # Compute the graph coloring using the Greedy algorithm
    color = greedy_graph_coloring(G)

    # Print the assigned color of each vertex
    print("Assigned colors:")
    for v in sorted(color):
        print("Vertex {}: color {}".format(v, color[v]))

if __name__ == "__main__":
    main()