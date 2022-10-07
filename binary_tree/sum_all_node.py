# https://www.geeksforgeeks.org/sum-nodes-binary-tree/
# TODO: 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BT:
    def __init__(self) -> None:
        self.root = None

bt = BT()
bt.root = Node(15)
bt.root.left = Node(10)
bt.root.right = Node(20)
bt.root.left.left = Node(8)
bt.root.left.right = Node(12)
bt.root.right.left = Node(16)
bt.root.right.right = Node(25)

# tot_sm = 0
def find_sum(root):
    # global tot_sm
    if root is None: return 0
    return root.data + find_sum(root.left) + find_sum(root.right)
    find_sum(root.right)
    tot_sm += root.data

# find_sum(bt.root)
print(find_sum(bt.root), "cool")