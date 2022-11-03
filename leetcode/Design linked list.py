class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0
        self.tail=None
    def len(self):
        len=0
        curr=self.head
        while curr!=None:
            curr= curr.next
            len +=1
        return len

    def get(self, index):
        length = self.len()
        if index+1 > length or index < 0:
            return -1
        elif index == 0:
            return self.head.val
        else:
            count = 0
            iterator = self.head
            while iterator.next:
                count += 1
                if count == index:
                    return iterator.next.val
                    break
                iterator = iterator.next 
    def addAtHead(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
        self.size +=1
        
    def addAtTail(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return

        iterator = self.head
        while iterator.next:
            iterator = iterator.next

        iterator.next = new_node
  
    def addAtIndex(self, index, val):
        len = self.len()
        if index < 0 or index > len:
            return None
        elif index ==0:
            self.addAtHead(val)
        elif index ==len:
            self.addAtTail(val)
        else:
            newnode=ListNode(val)
            curr=self.head
            for i in range(index-2):
                curr=curr.next
            newnode.next=curr.next
            curr.next=newnode
            self.size +=1
        
    def deleteAtIndex(self, index):
        len=self.len()
        iterator = self.head
        if index > len:
            return None
        elif index == 0:
            self.head = iterator.next
        else:
            count = 0
            
            while iterator.next:
                count += 1
                if count == index:
                    iterator.next = iterator.next.next
                    break

                iterator = iterator.next
       