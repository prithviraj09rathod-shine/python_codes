class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right

    def remove(self, node):
        pre, nxt = node.prev, node.next # temporary storing in these pre and nxt
        pre.next, nxt.prev = nxt, pre # removing the node by connecting its previous and next nodes

    def insert(self, node):
        pre, nxt = self.right.prev, self.right     # rightmost position
        pre.next = nxt.prev = node
        node.next, node.prev = nxt, pre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # removing this key value
            self.insert(self.cache[key]) #RE-inserting at the right most position place
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #before putting/inserting new value we are going to remove value from our list
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value) #making new node with the given key and value
        self.cache[key] = node   #copying Node(key,value) to self.cache[key]
        self.insert(node)      #insert(self.cache[key])

        if len(self.cache) > self.cap: # if cache size exceeds capacity
            lru = self.left.next # least recently used node will be at leftmost position
            self.remove(lru) # remove it from the doubly linked list
            del self.cache[lru.key] # remove it from the hashmap as well


capacity = 4
obj = LRUCache(capacity)
#obj.insert(5,50)
print(obj.put(1,10))
param1 = obj.get(1)
print(obj.put(2, 20))  # cache: {1=10, 2=20}
print(obj.put(3, 30))  # cache: {2=20, 3=30}, key=1 was evicted
print(obj.get(2))  
print(obj.get(3))    # returns 20  
#obj.remove()
""" LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);   
 """
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

""" 
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity:int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev=node
        node.next, node.prev=nxt, prev
    
    def get(self, key:int)->int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self,key:int, val:int)->None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
 """