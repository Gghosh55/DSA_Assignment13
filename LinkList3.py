class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:


    def __init__(self):
        self.head = None

    def reverse(self, head, k):

        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0


        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)


        return prev


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next



linklist = LinkedList()

linklist.push(8)
linklist.push(7)
linklist.push(6)
linklist.push(5)
linklist.push(4)
linklist.push(2)
linklist.push(2)
linklist.push(1)

print("Given linked list")
linklist.printList()
linklist.head = linklist.reverse(linklist.head, 4)

print("\nReversed Linked list")
linklist.printList()


