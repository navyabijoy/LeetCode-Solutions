class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # when we get, remove from the last and bring it forward and return
        node = self.hashmap[key]
        self._remove(node)
        self._insert_at_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        newNode = Node(key, value)
        self._insert_at_head(newNode)
        self.hashmap[key] = newNode

        if self.capacity < len(self.hashmap):
            # if the capacity is full, we remove the node before tail
            lru = self.tail.prev
            self._remove(lru)
            del self.hashmap[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)