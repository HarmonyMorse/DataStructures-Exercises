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

from queue import Queue

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
        # create a queue for nodes
        node_queue = Queue()

        # add the first node to the queue

        # while queue is not empty
        # remove the first node from the queue
        # print the removed node
        # add all children into the queue
        # ----

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
        # get the current node from the top of the stack
        # print that node
        # ---- the order you add the children matters
        pass

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
