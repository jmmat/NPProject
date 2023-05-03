import sys


def is_safe(vertex, color, coloring, g):
    for neighbor in g[vertex]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True


def min_graph_coloring(g):
    coloring = {}
    stack = [(list(g.keys()), 0, 0)]

    while stack:
        uncolored_vertices, vertex_idx, color = stack.pop()

        if vertex_idx == len(uncolored_vertices):
            continue

        vertex = uncolored_vertices[vertex_idx]

        if is_safe(vertex, color, coloring, g):
            coloring[vertex] = color
            stack.append((uncolored_vertices, vertex_idx + 1, 0))
            if vertex_idx + 1 == len(uncolored_vertices):
                break
        else:
            if color + 1 < len(set(coloring.values())) + 1:
                stack.append((uncolored_vertices, vertex_idx, color + 1))

    return len(set(coloring.values())), coloring


def is_valid_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if color == coloring[neighbor]:
                return False
    return True


def main(argv):
    # Read graph data from file
    with open(argv[0], 'r') as f:
        n = int(f.readline().strip())
        g = {}
        for line in f:
            u, v = line.split()
            u = u
            v = v
            if u not in g:
                g[u] = set()
            if v not in g:
                g[v] = set()
            g[u].add(v)
            g[v].add(u)

    colors, assigned_colors = min_graph_coloring(g)
    print(colors)
    for u in sorted(assigned_colors):
        print(u, assigned_colors[u])


if __name__ == "__main__":
    main(sys.argv[1:])
