Graph Coloring Program
This program uses a greedy algorithm to color the vertices of an undirected graph with the minimum number of colors such that no two adjacent vertices have the same color. The program reads the input graph from a text file and outputs the assigned color of each vertex, as well as the number of colors used.

Input Format
The input graph should be in the following format:

The first line should contain a single integer n, the number of vertices in the graph.
The following lines should contain pairs of integers u and v, indicating that there is an edge between vertex u and vertex v.
Example:

Copy code
4
1 2
2 3
3 4
4 1
This input represents a cycle graph with four vertices.

Output Format
The program outputs the following information:

Whether the coloring is valid (i.e., no adjacent vertices have the same color).
The number of colors used.
The assigned color of each vertex.
Example:

graphql
Copy code
True
2
4 1
3 2
2 1
1 2
This output indicates that the coloring is valid, two colors were used, and vertex 4 was assigned color 1, vertex 3 was assigned color 2, vertex 2 was assigned color 1, and vertex 1 was assigned color 2.

Running the Program
To run the program, open a terminal and navigate to the directory containing the program file (graph_coloring.py) and the input file. Then, run the following command:

Copy code
python graph_coloring.py input_file
where input_file is the path to the input file. For example, if the input file is in the same directory as the program file, you can run:

css
Copy code
python graph_coloring.py input.txt
This will run the program on the input graph specified in input.txt and output the results to the terminal.

