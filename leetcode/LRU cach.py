class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None   
    def addNode(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node       
        if self.tail is None:
            self.tail = node
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        else:
            return -1
    def removeNode(self, node):
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.next = None
        node.prev = None
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)

        else:
            if self.capacity > 0:
                self.capacity -=1
            else:
                del self.cache[self.tail.key]
                self.removeNode(self.tail)
            node = Node(key,value)
            self.cache[key] = node
            self.addNode(node)
       