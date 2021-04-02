##############
# NODE CLASS #
##############

class Node:
    name: str
    long: float
    lat: float

    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat

    def distance(self, other):
        pass

#############
# BACA FILE #
#############
file = open("Tucil3/test.txt")
fileContent = file.readlines()
file.close()
fileContent = [x.strip() for x in fileContent]

nodeCount = int(fileContent[0])

##########################
# BIKIN LIST NODES #
##########################
nodes = []
for i in range (1,nodeCount+1):
    lines = fileContent[i].split()
    node = Node(lines[0], lines[1], lines[2])
    nodes += [node]

#######################
# BIKIN MATRIKS EDGES #
#######################
edges = []
for i in range (nodeCount+1, nodeCount*2+1):
    edge = fileContent[i].split()
    edges += [[float(j) for j in edge]]



print(edges)
for n in nodes:
    print(n.name, n.long, n.lat)