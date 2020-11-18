class Edge:

    def __init__(self, Id, v1_id, v2_id, cost):
        self.Id = Id
        self.v1_id = v1_id
        self.v2_id = v2_id
        self.cost = cost

    def __str__(self):
        return "Edge:{}, Vertices:({},{}), Cost:{}".format(self.Id,self.v1_id,self.v2_id,self.cost)
