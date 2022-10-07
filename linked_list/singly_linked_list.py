class Node:
    def __init__(self, val, next=None):
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
    
    def reverse(self):
        # 1->2->3->None
        # None<-1<-2<-3
        prev = None
        cur = self.head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

sl = SingleLinkedList()
sl.insert(1)
sl.insert(2)
sl.insert(3)
sl.insert(4)
sl.insert(5)
sl.insert(6)
sl.display()

sl.reverse()
print("\nhere goes reversed Linked list")
sl.display()