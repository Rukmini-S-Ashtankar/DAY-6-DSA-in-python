# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

# LinkedList = LinkedList()

# LinkedList.head() = Node(5)
# second            = Node(10)
# third             = Node(15)
# fourth            = Node(20)

# # Connecting nodes
# LinkedList.head.next = second
# second.next = third
# third.next = fourth

# # Display LinkedList
# while LinkedList.head != None:
#     print(LinkedList.head.data, "|", LinkedList.head.next, "-->", end = " ")
#     LinkedList.head = LinkedList.head.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


LinkedList = LinkedList()

LinkedList.head = Node(5)
second = Node(10)
third = Node(15)
fourth = Node(20)

# Connecting nodes
LinkedList.head.next = second
second.next = third
third.next = fourth

# Display Linked List
temp = LinkedList.head

while temp != None:
    print(temp.data, "-->", end=" ")
    temp = temp.next                                         # cgt