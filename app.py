from edge import Edge
from node import Node
from algorithm import Algorithm
import mapdata

algorithm = Algorithm()
start = mapdata.user_start_node
end = mapdata.node7

algorithm.calculateShortestPath(mapdata.vertexList, start)
algorithm.getShortestPath(start, end)
