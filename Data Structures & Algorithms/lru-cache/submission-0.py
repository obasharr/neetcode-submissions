class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert_at_head(node)

        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value

            self.remove(node)
            self.insert_at_head(node)
        else:
            if len(self.map) == self.capacity:
                lru = self.tail.prev
                del self.map[lru.key]
                self.remove(lru)
            new_node = Node(key, value)
            self.map[key] = new_node
            self.insert_at_head(new_node)

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_at_head(self, node: Node) -> None:
        node.next = self.head.next
        node.next.prev = node

        self.head.next = node
        node.prev = self.head
        
