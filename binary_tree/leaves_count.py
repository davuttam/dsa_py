# Count Leaves in Binary Tree
# Given a Binary Tree of size N , You have to count leaves in it. For example, there are two leaves in following tree
# https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1?page=2&difficulty[]=-1&sortBy=submissions

# TODO:

def countLeaves(root):
    if root is None: return 0
    elif root.left == None and root.right == None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)