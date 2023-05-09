import sys
import time
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


def main(filename):
    print(filename)
    g = graph_from_file(filename)
    start_time = time.time()
    colors, assigned_colors = min_graph_coloring(g)
    elapsed_time = time.time() - start_time
    start_time = time.time()
    print(f"Elapsed time: {elapsed_time:.5f} seconds")
    print(
        f"Is valid solution: {check_valid_coloring(g, assigned_colors)}\nNumber of colors: {colors}")


if __name__ == "__main__":
    main(sys.argv[1])
