class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node 
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)


ll = LinkedList()
ll.insert_at_begining("2")
ll.insert_at_begining("4")
ll.insert_at_end("69420")
ll.print()