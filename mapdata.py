from edge import Edge
from node import Node

more = True

room = []

while more:
	vertex_name = input("\nEnter rooms affected: ")
	room.append(vertex_name)
	more = input("\nAre there any more rooms? Y/N: ")
	if more == 'N' or more == 'n':
		more = False

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5, node1, node2, room)
edge2 = Edge(8, node1, node8, room)
edge3 = Edge(9, node1, node5, room)
edge4 = Edge(15, node2, node4, room)
edge5 = Edge(12, node2, node3, room)
edge6 = Edge(4, node2, node8, room)
edge7 = Edge(7, node8, node3, room)
edge8 = Edge(6, node8, node6, room)
edge9 = Edge(5, node5, node8, room)
edge10 = Edge(4, node5, node6, room)
edge11 = Edge(20, node5, node7, room)
edge12 = Edge(1, node6, node3, room)
edge13 = Edge(13, node6, node7, room)
edge14 = Edge(3, node3, node4, room)
edge15 = Edge(11, node3, node7, room)
edge16 = Edge(9, node4, node7, room)

edge17 = Edge(5, node2, node1, room)
edge18 = Edge(8, node8, node1, room)
edge18 = Edge(8, node8, node1, room)
edge19 = Edge(9, node5, node1, room)
edge20 = Edge(15, node4, node2, room)
edge21 = Edge(12, node3, node2, room)
edge22 = Edge(4, node8, node2, room)
edge23 = Edge(7, node3, node8, room)
edge24 = Edge(6, node6, node8, room)
edge25 = Edge(5, node8, node5, room)
edge26 = Edge(4, node6, node5, room)
edge27 = Edge(20, node7, node5, room)
edge28 = Edge(1, node3, node6, room)
edge29 = Edge(13, node7, node6, room)
edge30 = Edge(3, node4, node3, room)
edge31 = Edge(11, node7, node3, room)
edge32 = Edge(9, node7, node4, room)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge4)
node2.adjacenciesList.append(edge5)
node2.adjacenciesList.append(edge6)
node8.adjacenciesList.append(edge7)
node8.adjacenciesList.append(edge8)
node5.adjacenciesList.append(edge9)
node5.adjacenciesList.append(edge10)
node5.adjacenciesList.append(edge11)
node6.adjacenciesList.append(edge12)
node6.adjacenciesList.append(edge13)
node3.adjacenciesList.append(edge14)
node3.adjacenciesList.append(edge15)
node4.adjacenciesList.append(edge16)

node2.adjacenciesList.append(edge17)
node8.adjacenciesList.append(edge18)
node5.adjacenciesList.append(edge19)
node4.adjacenciesList.append(edge20)
node3.adjacenciesList.append(edge21)
node8.adjacenciesList.append(edge22)
node3.adjacenciesList.append(edge23)
node6.adjacenciesList.append(edge24)
node8.adjacenciesList.append(edge25)
node6.adjacenciesList.append(edge26)
node7.adjacenciesList.append(edge27)
node3.adjacenciesList.append(edge28)
node7.adjacenciesList.append(edge29)
node4.adjacenciesList.append(edge30)
node7.adjacenciesList.append(edge31)
node7.adjacenciesList.append(edge32)

vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)

room_data = {"A" : node1, "B" : node2, "C" : node3, "D" : node4, "E" : node5, "F" : node6, "G" : node7, "H" : node8}

user_start_room = input("\nEnter your room name: ")
user_start_node = room_data[user_start_room]