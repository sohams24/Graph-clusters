from Graph import Graph

g = Graph('data.txt')
no_of_clusters = 4
g.clustering(no_of_clusters)
f = open('Clusters.txt','w')
for cluster in g.clusters.values():
    for vertex in cluster:
        f.write(vertex)
        f.write(" ")
    f.write("\n\n\n")
f.close()
