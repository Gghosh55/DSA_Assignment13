class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = None

    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next

        ptr.next = temp

    return root



def newList(root1, root2):
    ptr1 = root1
    ptr2 = root2

    root = None
    while (ptr1 != None):
        temp = Node(0)
        temp.next = None

        # Compare for greater node
        if (ptr1.data < ptr2.data):
            temp.data = ptr2.data
        else:
            temp.data = ptr1.data

        if (root == None):
            root = temp
        else:
            ptr = root
            while (ptr.next != None):
                ptr = ptr.next

            ptr.next = temp

        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return root


def display(root):
    while (root != None):
        print(root.data, "->", end=" ")
        root = root.next

    print(" ");



if __name__ == '__main__':
    root1 = None
    root2 = None
    root = None


    root1 = insert(root1, 5)
    root1 = insert(root1, 2)
    root1 = insert(root1, 3)
    root1 = insert(root1, 8)

    print("First List: ", end=" ")
    display(root1)


    root2 = insert(root2, 1)
    root2 = insert(root2, 7)
    root2 = insert(root2, 4)
    root2 = insert(root2, 5)

    print("Second List: ", end=" ")
    display(root2)

    root = newList(root1, root2)
    print("New List: ", end=" ")
    display(root)


