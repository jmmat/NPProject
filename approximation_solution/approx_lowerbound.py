import sys

def is_valid_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if color == coloring[neighbor]:
                return False
    return True

def greedy_graph_coloring(G):
    color = {} 
    for v in range(len(G)):
        used_colors = set(color[u] for u in G[v+1] if u in color and u != v + 1)
        if not used_colors:
            color[v+1] = 0 
        else:
            color[v+1] = min(c for c in range(1, len(G)+1) if c not in used_colors)
    return color

def lower_bound(G):
    # Calculate the maximum degree in the graph
    delta = max(len(G[v]) for v in G)
    # The lower bound is delta + 1
    return delta + 1

def main():
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

    # Calculate the lower bound
    lb = lower_bound(G)

    # Print the assigned color of each vertex and the lower bound
    print("Number of colors used:", len(set(color.values())))
    print("Lower bound:", lb)

    for v in sorted(color, reverse=True):
        print(v, color[v])

if __name__ == "__main__":
    main()