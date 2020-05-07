import heapq


class Algorithm:

    def calculateShortestPath(self, vertexList, startVertex):
        q = []
        startVertex.minDistance = 0
        heapq.heappush(q, startVertex)

        while q:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(q, v)

    def getShortestPath(self, startVertex, targetVertex):
        print(
            f'\n\nShortest path distance from {startVertex.name} to {targetVertex.name} is {targetVertex.minDistance}')

        actualList = []

        node = targetVertex

        while node is not None:
            actualList.append(node.name)
            node = node.predecessor

        print("\nSAFER - SHORTEST PATH ROUTE: ", end="")

        for i in range(len(actualList) - 1, -1, -1):
            print(actualList[i] + " -> ", end="")

        print("\b\b\b   ")
