class Node:
    def __init__(self, val, minimum, next_node):
        self.val = val
        self.min = minimum
        self.next = next_node

class MinStack:

    def __init__(self):
        self.head = None 

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val, None)

        else:
            self.head = Node(
                val,
                min(val, self.head.min),
                self.head
            )

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min
