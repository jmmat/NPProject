import time

from exact_util import graph_from_file, min_graph_coloring, check_valid_coloring, generate


def main():
    for i in range(5, 30, 1):
        print(f"for {i} minimum colors")
        generate(i, i)
        g = graph_from_file(f"./Data/graph_{i}_edges_{i}_colors.txt")
        start_time = time.time()
        colors, assigned_colors = min_graph_coloring(g)
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.5f} seconds")
        print(f"{check_valid_coloring(g, assigned_colors)} {colors}\n")


if __name__ == "__main__":
    main()
