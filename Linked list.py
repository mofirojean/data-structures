"""Algorithm for a linked list"""


class Node:
    """this class contains the attributes of the node in a linked list"""
    """each element in the linked list is stored in a node.
    a node is a collection of two sub-elements or parts
    'a data part' that stores the element and 
    'a next part' that links the next node
    the linked list is formed when many nodes are connected in a chain"""

    def __init__(self, data, pointer=None):
        self.next = pointer
        self.data = data

    # def __str__(self):
    #     return "{0} -> {1}".format(self.data, self.next)


class LinkedList:
    """performs the operations of a linked list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            ll_str = "["
            curr = self.head
            while curr is not None:
                ll_str = ll_str + str(curr.data) + " -> "
                curr = curr.next
            ll_str = ll_str + "None]"
            return ll_str

    """method inserts data as the head"""

    def insert_n(self, new_node):
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def is_empty(self):
        return self.head is None


jean = Node("Jean")
kimbi = Node("Kimbi")
des = Node("Desmond")

my_ll = LinkedList()
my_ll.insert_n(jean)
my_ll.insert_n(kimbi)
my_ll.insert_n(des)

print(my_ll)
