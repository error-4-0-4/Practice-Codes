# PUSH ELEMENT IN THE FRONT
# PRINT WHOLE LL
# FIND MIDDLE OF THE LINKED LIST
# SLOW POINTER APPROACH - WHEN FAST.NEXT IS NULL RETURN SLOW

class Node:
    #initialize node object
    def __init__ (self, data):
        self.data=data
        self.next=None

class LinkedList():

    #initialize head
    def __init__(self):
        self.head=None

    #insert node in the beggining
    def push(self, n_data):
        n_node=Node(n_data)
        n_node.next=self.head
        self.head=n_node
    
    #print list
    def printlist(self):
        node= self.head
        while node:
            print(str(node.data)+"->", end=" ")
            node= node.next
        print("NULL")

    #find middle ele
    def printmid(self):
        slow=self.head
        fast = self.head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        
        print("Middle ele:", slow.data)

if __name__ == '__main__':
    ll = LinkedList()

    for i in range (5,0,-1):
        ll.push(i)
    ll.printlist()
    ll.printmid()