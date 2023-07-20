"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node that corresponds to our first node in the list
        self.tail = None  # Stores a node that corresponds to our last node in the list

    def __str__(self):
        output = ''
        current_node = self.head  # create a tracker node variable
        while current_node is not None:  # loop until it's None
            output += f'{current_node.value} -> '
            current_node = current_node.next_node  # update the tracker node to the next node
        return output

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to current head
            new_node.next_node = self.head
            # move head to a new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return
        # if list only has one element, set head and tail to none
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        while current_node is not None:
            # Check if it's the node we're looking for
            if current_node.value == value:
                return True
            # Otherwise, go to the next node
            current_node = current_node.next_node
        return False


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add the new value to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of the list
        self.size -= 1
        value = self.storage.remove_head()
        return value


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
            # return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
                return
            self.left = new_node
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
                return
            self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        if target >= self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        node_queue = Queue()
        node_queue.enqueue(self)
        while not len(node_queue) == 0:
            current_node = node_queue.dequeue()
            print(current_node.value)
            if current_node.left is not None:
                node_queue.enqueue(current_node.left)
            if current_node.right is not None:
                node_queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack for nodes
        node_stack = Stack()
        # add the first node to the stack
        node_stack.push(self)
        # while the stack is not empty
        while not len(node_stack) == 0:
            # get the current node from the top of the stack
            current_node = node_stack.pop()
            # print that node
            print(current_node.value)
            # ---- the order you add the children matters
            if current_node.left is not None:
                node_stack.push(current_node.left)
            if current_node.right is not None:
                node_stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)
#
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
#
# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
