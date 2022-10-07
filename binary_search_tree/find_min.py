# Minimum element in BST
# TODO: https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1?page=2&difficulty[]=-1&sortBy=submissions

import math
#Function to find the minimum element in the given BST.
def minValue(root):
    min_val = math.inf
    def find_min(root):
        nonlocal min_val
        ##Your code here
        # print(root)
        if root is None:
            return
        find_min(root.left)
        if root.data < min_val:
            min_val = root.data
        
        find_min(root.right)
    find_min(root)
    return min_val

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.head = None

bst = BST()
node = Node(5)
bst.head = node
bst.head.left = Node(4)
bst.head.right = Node(6)
bst.head.left.left = Node(3)
bst.head.right.right = Node(7)
bst.head.left.left.left = Node(1)


print(minValue(bst.head))