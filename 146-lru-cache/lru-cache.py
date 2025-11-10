class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}  # key: node

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_head(self, node): 
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    
    def remove_from_end(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if not key in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove_from_end(node)
        self.add_to_head(node)
        return node.val   

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove_from_end(node)
            self.add_to_head(node)
        else: #if not in the map
            newNode = Node(key, value)
            self.hashmap[key] = newNode
            self.add_to_head(newNode)

        if len(self.hashmap) > self.capacity:
            lru = self.tail.prev
            self.remove_from_end(lru)
            del self.hashmap[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)