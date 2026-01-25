
class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.current = None

    def createNode(self, data):
        newNode = Node()
        newNode.data = data
        newNode.next = self.current
        self.current = newNode

    def display(self):
        node = self.current
        while node:
            print(node.data, end=" ")
            node = node.next

list = LinkedList()
list.createNode(1)
list.createNode(2)
list.createNode(3)

list.display()