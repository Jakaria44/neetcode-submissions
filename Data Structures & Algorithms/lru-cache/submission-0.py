class LRUCache:
    class DoublyLinkedListNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = self.prev = None
        
    def add_to_tail(self, node):
        temp = self.tail.prev

        node.prev = temp
        node.next = self.tail
        
        temp.next = node
        self.tail.prev = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def __init__(self, capacity: int):
        self.capacity = capacity    
        self.hashmap = {}

        self.head = self.DoublyLinkedListNode(-1,-1)
        self.tail = self.DoublyLinkedListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
 

    def get(self, key: int) -> int:

        if key not in self.hashmap:
            return -1
        
        self.remove_node(self.hashmap[key])
        self.add_to_tail(self.hashmap[key])
        
        return self.hashmap[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])

        node = self.DoublyLinkedListNode(key,value)

        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)


        
