class Node:


    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



def deleteNode(head_ref, del_):

    if (head_ref == None or del_ == None):
        return


    if (head_ref == del_):
        head_ref = del_.next


    if (del_.next != None):
        del_.next.prev = del_.prev


    if (del_.prev != None):
        del_.prev.next = del_.next

    return head_ref



def deleteNodeAtGivenPos(head_ref, n):

    if (head_ref == None or n <= 0):
        return

    current = head_ref
    i = 1


    while (current != None and i < n):
        current = current.next
        i = i + 1


    if (current == None):
        return


    deleteNode(head_ref, current)

    return head_ref



def push(head_ref, new_data):

    new_node = Node(0)


    new_node.data = new_data


    new_node.prev = None


    new_node.next = (head_ref)


    if ((head_ref) != None):
        (head_ref).prev = new_node


    (head_ref) = new_node

    return head_ref



def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


head = None

head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)

print("Doubly linked list before deletion:")
printList(head)

n = 2

head = deleteNodeAtGivenPos(head, n)

print("\nDoubly linked list after deletion:")

printList(head)


