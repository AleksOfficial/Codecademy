class Vertex:
  def __init__(self, value):
    
    self.value = value
    self.edges = {}

  def add_edge(self, vertex):
    self.edges[vertex] = True

  def get_edges(self):
    return list(self.edges.keys())

  def __repr__(self):
      d = [k for k,v in globals().items() if v is self]    
      #d = {v:k for k,v in globals().items()}
      return str(d[0])

class Graph:
  def __init__(self,directed = False):
    self.directed = directed
    self.graph_dict = {}
  
  def add_vertex(self,vertex):
    print("Adding "+ vertex.value)
    self.graph_dict[vertex.value] = vertex



grand_central = Vertex("Grand Central Station")

# Uncomment this code after you've defined Graph
railway = Graph()

# Uncomment these lines after you've completed .add_vertex()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)