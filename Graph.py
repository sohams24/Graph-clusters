from Vertex import Vertex
from Edge import Edge
import random

class Graph:

    def __init__(self, filename, debug=False):

        self.edges = dict()
        self.vertices = dict()
        self.current_vertices = {}
        self.clusters = dict()

        with open(filename,'r') as f:
            self.no_of_vertices = int(f.readline().strip())
            edge_id_count = 1
            for line in f:
                line_arr = line.strip().split()
#                 line_arr = [int(x) for x in line_arr]
                cost = int(line_arr.pop())
                for v_id in line_arr:
                    if v_id not in self.vertices:
                        new_vertex = Vertex(v_id,edge_id_count)
                        self.vertices[v_id] = new_vertex
                        self.clusters[v_id] = [v_id]
                    else:
                        self.vertices[v_id].update_edges(edge_id_count)
                new_edge = Edge(edge_id_count,line_arr[0],line_arr[1],cost)
                self.edges[edge_id_count] = new_edge
                edge_id_count+=1




    def clustering(self, target, debug=False):
        no_of_clusters = self.no_of_vertices
        if debug:
            print("No of clusters at start: ",no_of_clusters)
        sorted_edges = sorted(list(self.edges.values()), key=lambda x:x.cost, reverse=False)
        if debug:
            print("Following are edges in sorted order:\n")
            for edge in sorted_edges:
                print(edge)

        for edge in sorted_edges:
            v1 = self.vertices[edge.v1_id]
            v2 = self.vertices[edge.v2_id]
            if v1.leader_id != v2.leader_id:
                if debug:
                    print("\nFollowing are currently the 2 closest points from different clusters:")
                    print(v1)
                    print(v2)
                if debug:
                    print("The current no of clusters is: ",no_of_clusters)
                if no_of_clusters == target:
                    if debug:
                        print("No of clusters has met the target")
                    return edge.cost
                if self.vertices[v1.leader_id].rank > self.vertices[v2.leader_id].rank:
                    source = self.vertices[v2.leader_id]
                    dest = self.vertices[v1.leader_id]
                else:
                    source = self.vertices[v1.leader_id]
                    dest = self.vertices[v2.leader_id]

                if debug:
                    print("Merging {} into {}".format(source.Id,dest.Id))

                self.merge_cluster(dest,source,debug)
                no_of_clusters -= 1


    def merge_cluster(self,dest,source,debug=False):
        if debug:
            print("Extending slaves list of {} by slaves list of {}".format(dest.Id,source.Id))

        self.clusters[dest.Id].extend(self.clusters[source.Id])
        del self.clusters[source.Id]
        dest.slaves.extend(source.slaves)
        if debug:
            print("New slaves list of ",dest.Id)
            for slave in dest.slaves:
                print(slave)
        dest.rank += source.rank
        if debug:
            print("New rank of {} is {}".format(dest.Id,dest.rank))
        for slave in source.slaves:
            slave.leader_id = dest.Id
            if debug:
                print("Updated leader of {} to {}".format(slave.Id,dest.Id))
        source.slaves.clear()


    def __str__(self):
        s="The Edges are as follows:\n"
        for edge in g.edges.values():
            s += edge.__str__() + "\n"
        s+="\nThe Vertices are as follows:\n"
        for vertex in g.vertices.values():
            s += vertex.__str__() + "\n"
        return s
