class ListNode:
    def __init__ (self,key=-1,value=-1, next=None):
        self.key =key
        self.next = next
        self.val = value


class MyHashMap:

    def __init__(self):
        self.data_map = [ListNode() for i in range(10000)]

    def hash(self,key):
        return key % len(self.data_map) #to create a key value
    
    def put(self, key: int, value: int) -> None:
        cur = self.data_map[self.hash(key)]
        while cur.next: #while the list continues
            if cur.next.key == key: #while the key exist in the hashmap
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        cur = self.data_map[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1


    def remove(self, key: int) -> None:
        cur = self.data_map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)