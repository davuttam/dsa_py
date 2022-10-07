class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.next
    
    def insert(self, val):
        curr = self.head
        node = Node(val)
        if curr is not None:
            while curr.next != None:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

# args are head
def merge_two_sorted_list(sl1, sl2):
    cur1, cur2 = sl1.head, sl2.head
    sl3 = SingleLinkedList()

    while cur1 != None or cur2 != None:
        if cur1 != None and cur2 != None:
            if cur1.val < cur2.val:
                cur = cur1
                cur1 = cur1.next
            else:
                cur = cur2
                cur2 = cur2.next
        elif cur1 == None:
            cur = cur2
            cur2 = cur2.next
        else:
            cur = cur1
            cur1 = cur1.next

        if sl3.head is None:
            sl3.head = cur
            trail = sl3.head
        else:
            trail.next = cur
            trail = trail.next

    return sl3

sl = SingleLinkedList()
sl.insert(1)
sl.insert(2)
sl.insert(4)
sl.display()

print("")
sl1 = SingleLinkedList()
sl1.insert(1)
sl1.insert(3)
sl1.insert(4)
sl1.display()

sl2 = merge_two_sorted_list(sl, sl1)
print("")
sl2.display()