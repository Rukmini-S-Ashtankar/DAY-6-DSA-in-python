# class Node:
#     def __init__ (self, data):
#         self.data = data 
#         self.next = None

# class linkedList:
#     def __init__(self):
#         self.head = None
#         self.next = None

#     def addNode(self, value):
#         self.node = Node(value)
#         if  self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail = self.node

#     def addNodeBeginning(self, value):
#         print("Add node at beginning: ")
#         self.node = Node(value)
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.node.next = self.head

#     def addNodeBetween(self, index, value):
#         if
#             self.head = self.node
#             self.tail = self.node
#         elif index == 0:
#             node.next = self.head


         

#     def displayNode(self):
#         while self.head is not None:
#              print(self.head.data, '|', self.head.next, '->', end = ' ')
#              self.head = self.head.next

# if __name__ == '__main__':
#     object = linkedList()

# while True:
#     print("1. Add node to LinkedList: ")
#     print("2. Add node in beginning: ")
#     print("3. Add node in between: ")
#     print("4. Add node in the End: ")
#     print("5. Display the LinkedList: ")
#     print("6. Exit ")

#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#          value = int(input("Enter value for nodes: "))
#          object.addNode(value)
#          print("Node added successfully in single Linkedist ")

#     elif ch == 2:
#             value(int(input("Enter a node to add in the beginning: ")))

#     elif ch == 3:
#          value(int(input(" Enter node to add in between: ")))
         
#     elif ch == 4:
#          value(int(input("Enter node to add at the end: ")))

#     elif ch == 5:
#         self.displayNode()
   

#     elif ch == 6:
#             print(" Exit ")
#             break
#     else:
#             print("Invalid choice")


# =========================== CHAT GPT ===========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node at end
    def addNode(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Add node at beginning
    def addNodeBeginning(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    # Add node at a specific position
    def addNodeBetween(self, index, value):
        node = Node(value)

        if index == 0:
            self.addNodeBeginning(value)
            return

        temp = self.head
        count = 0

        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid index")
        else:
            node.next = temp.next
            temp.next = node

            if node.next is None:
                self.tail = node

    # Display linked list
    def displayNode(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


if __name__ == '__main__':

    obj = LinkedList()

    while True:
        print("\n1. Add node to LinkedList")
        print("2. Add node in beginning")
        print("3. Add node in between")
        print("4. Add node at the end")
        print("5. Display the LinkedList")
        print("6. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1 or ch == 4:
            value = int(input("Enter value for node: "))
            obj.addNode(value)
            print("Node added successfully")

        elif ch == 2:
            value = int(input("Enter node value to add at beginning: "))
            obj.addNodeBeginning(value)
            print("Node added at beginning")

        elif ch == 3:
            index = int(input("Enter position index: "))
            value = int(input("Enter node value: "))
            obj.addNodeBetween(index, value)
            print("Node added in between")

        elif ch == 5:
            obj.displayNode()

        elif ch == 6:
            print("Exit")
            break

        else:
            print("Invalid choice")



