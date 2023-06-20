class Node:
    def __init__(self, data):
	    self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None


	def reverseUsingStacks(self):

		stack = []
		temp = self.head
		while temp is not None:
			stack.append(temp.data)
			temp = temp.next


		temp = self.head
		while temp is not None:
			temp.data = stack.pop()
			temp = temp.next



	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head

		if self.head is not None:
			self.head.prev = new_node

		self.head = new_node



	def printList(self, node):
		while(node is not None):
			print(node.data)
			node = node. next



if __name__ == "__main__":
	dll = DoublyLinkedList()
	dll.push(2)
	dll.push(4)
	dll.push(8)
	dll.push(10)

	print("original doubly-linked list")
	dll.printList(dll.head)


	dll.reverseUsingStacks()

	print(" reversed doubly-linked list")
	dll.printList(dll.head)
