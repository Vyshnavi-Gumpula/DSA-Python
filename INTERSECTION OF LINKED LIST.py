class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else: 
            temp = self.head
            while temp.next is not None:
                if temp.data == 30:
                    newnode.next = temp.next
                    temp.next = newnode
                    return
                temp = temp.next
            temp.next = newnode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def intersection_of_2linkedlist(self, other):
        t1 = self.head
        t2 = other.head
        while t1 != t2:
            t1 = t1.next if t1 else other.head
            t2 = t2.next if t2 else self.head
        if t1:
            print("Intersection at node with data:", t1.data)
        else:
            print("No intersection")

# Create l2
l2 = LinkedList()
l2.head = node(100)
l2.head.next = node(200)
intersect_node = node(300)
l2.head.next.next = intersect_node
intersect_node.next = node(400)
intersect_node.next.next = node(500)

# Create l1 and intersect at node 300
l1 = LinkedList()
l1.head = node(10)
l1.head.next = node(20)
l1.head.next.next = intersect_node  # intersection here

# Display both
print("Linked List 1:")
l1.display()
print("Linked List 2:")
l2.display()

# Find intersection
l1.intersection_of_2linkedlist(l2)