import sys

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex, room):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex

		if self.startVertex.name in room or self.targetVertex.name in room:
			self.weight = sys.maxsize
		