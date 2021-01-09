# Graph-clusters
In this project we find clusters of closely spaced points based on their eucleadean distances using a greedy algorithm. The points are represented in the form of a complete graph with vertices as the points and the edges represent the eucleadean distance between two points.
The input graph is provided in the file "data.txt". The first line indicates total number of points. From the second line onwards, the first two values represent the two end points followed by the euclidean distance between the points.

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Add your input text file to the folder (the graph in your input file should have the format same as the one in "data.txt")
3)  Specify the name of your input file in the file "main.py" on line 3.
4)  Run the file "main.py".
5)  Check the file "Clusters.txt" for the output.

Edge.py:
This file defines the "Edge" class.
Every edge has an "id" two end vertices named "v1" and "v2" and an edge-cost.

Vertex.py:
This file defines the "Vertex" class.
Every vertex has an "id", and a list "edges" that stores the "ids" of all the edges incident to that vertex.

Graph.py:
This file defines the "Graph" class.
The graph has two dictonary named "edges" and "vertices" which stores all the edge and vertex instances with their respective "ids" as keys.

main.py:
This is the file that creates the "Graph" instance by passing the input file.
Here we call the "clustering" method on the graph instance and the output file.