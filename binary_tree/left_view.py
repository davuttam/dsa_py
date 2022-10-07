# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
# TODO:

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def print_left_view(root, cur_level):
    global max_level
    if root == None: return
    if max_level < cur_level:
        print(root.val)
        max_level = cur_level

    print_left_view(root.left, cur_level+1)
    print_left_view(root.right, cur_level+1)

root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)

max_level = 0
print_left_view(root, 1)