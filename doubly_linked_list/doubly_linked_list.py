"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.length += 1
            self.head = new_node
            self.tail = new_node
        else:
            self.length += 1
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return
        if self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node.value
        node = self.head
        self.head = node.next
        self.head.prev = None
        node.next = None
        self.length -= 1
        return node.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return
        elif self.length == 1:
            old_node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return old_node.value
        else:
            old_node = self.tail
            new_tail = old_node.prev
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return old_node.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            return
        if self.length >= 2:
            current_node = self.tail
            while current_node is not node:
                current_node = current_node.prev
            if current_node.next is not None and current_node.prev is not None:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            current_node.next = self.head
            current_node.prev = None
            self.head.prev = current_node
            self.head = current_node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            return
        if self.length >= 2:
            current_node = self.head
            while current_node.value is not node.value:
                current_node = current_node.next
            if current_node.prev is not None and current_node.next is not None:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
            current_node.prev = self.tail
            if current_node is self.head:
                self.head = current_node.next
            current_node.next = None
            self.tail.next = current_node
            self.tail = current_node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        current_node = self.head
        while current_node is not node:
            current_node = current_node.next
        if current_node is self.head:
            self.head = current_node.next
            self.head.prev = None
            self.length -= 1
        elif current_node is self.tail:
            self.tail = current_node.prev
            self.tail.next = None
            self.length -= 1
        else:
            current_node.next.prev = current_node.prev
            current_node.prev.next = current_node.next
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        current_node = self.head
        max_value = self.head.value
        while True:
            if current_node.value > max_value:
                max_value = current_node.value
            if current_node.next is None:
                break
            current_node = current_node.next
        return max_value
