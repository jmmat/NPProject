import time
import random
import itertools


def is_valid_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if color == coloring[neighbor]:
                return False
    return True


def min_graph_coloring(g):
    n = len(g.keys())
    for k in range(1, n+1):
        for coloring in itertools.product(range(k), repeat=n):
            vertex_color_map = dict(zip(g.keys(), coloring))
            if is_valid_coloring(g, vertex_color_map):
                return k, vertex_color_map


def check_valid_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if color == coloring[neighbor]:
                return False
    return True


def graph_from_file(filename):
    g = {}
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for line in f:
            u, v = line.split()
            if u not in g:
                g[u] = set()
            if v not in g:
                g[v] = set()
            g[u].add(v)
            g[v].add(u)
    return g


def generate_random_graph(x, min_colors):
    max_vertexes = x + 1
    edges = set()

    # Create a clique with min_colors number of vertices
    vertices = list(range(1, min_colors + 1))
    for i in range(min_colors):
        for j in range(i + 1, min_colors):
            v1 = vertices[i]
            v2 = vertices[j]
            edges.add((v1, v2))

    # Add the remaining edges randomly
    while len(edges) < x:
        v1 = random.randint(1, max_vertexes)
        v2 = random.randint(1, max_vertexes)

        if v1 != v2 and (v1, v2) not in edges and (v2, v1) not in edges:
            edges.add((v1, v2))

    return edges


def write_graph_to_file(graph, filename):
    with open(filename, 'w') as f:
        f.write(f"{len(graph)}\n")
        for edge in graph:
            f.write(f"{edge[0]} {edge[1]}\n")


def generate(edges, min_colors):
    num_edges = int(edges)
    random_graph = generate_random_graph(num_edges, int(min_colors))
    output_file = f"./Data/graph_{num_edges}_edges_{min_colors}_colors.txt"
    write_graph_to_file(random_graph, output_file)


def main():
    N = int(input())
    g = {}
    for _ in range(N):
        u, v = input().split()
        if u not in g:
            g[u] = set()
        if v not in g:
            g[v] = set()
        g[u].add(v)
        g[v].add(u)
    colors, assigned_colors = min_graph_coloring(g)
    print(colors)
    for u in assigned_colors:
        print(u, assigned_colors[u])


if __name__ == "__main__":
    main()
