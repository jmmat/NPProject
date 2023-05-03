Greedy-Graph-Coloring(G):
    color = empty set
    for each vertex v in G:
        used_colors = set of colors used by v's neighbors
        if used_colors is empty:
            color[v] = 1
        else:
            color[v] = min {c ∈ N : c not in used_colors}
        add color[v] to color set
    return color
