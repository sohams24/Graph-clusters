class Vertex:

    def __init__(self, Id, edge_id):
        self.Id = Id
        self.edges = [edge_id]
        self.leader_id = Id
        self.rank = 1
        self.slaves = [self]

    def update_edges(self, new_edge_id):
        self.edges.append(new_edge_id)

    def __str__(self):
        s="Vertex:{},\t".format(self.Id)
        s+= "Incident edges: ["
        for i in range(len(self.edges)):
            s+=str(self.edges[i])
            if i+1 == len(self.edges):
                s+=']'
            else:
                s+=', '
        return s
