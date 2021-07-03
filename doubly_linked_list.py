# doubly linked list add, remove and size of doubly linked list

# create nodes for doubly linked list which has a prev and a next node
class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


# create a doubly_linked list with head and tail and initial size is 0
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    # add element to the list
    def add(self, value):
        node = Node(value)

        if self.tail is None:  # list is empty so value head and tail refers to same node
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:  # 1st node to delete
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:   # last node to delete
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.value == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals = []
        node = self.head

        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list = DoublyLinkedList()
my_list.add(5)
my_list.add(3)
print(my_list)