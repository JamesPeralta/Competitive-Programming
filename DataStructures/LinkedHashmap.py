class Node:
    def __init__(self, key=None, value=float("inf"), prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LinkedHashmap:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}
        self.length = 0

    def __len__(self):
        return self.length

    def move_to_end(self, key):
        node = self.hash_map[key]
        self.remove_node(node)
        self.append_node(self.tail.prev, node)

    def pop_left(self):
        head = self.head.next
        node = self.remove_node(head)
        key = node.key
        del self.hash_map[key]
        self.length -= 1

    def get(self, key):
        return self.hash_map[key].value

    def put(self, key, value):
        node = Node(key, value)
        self.append_node(self.tail.prev, node)
        self.hash_map[key] = node
        self.length += 1

    def update(self, key, val):
        self.hash_map[key].value = val

    def append_node(self, prev, node):
        node.next = prev.next
        node.prev = prev
        prev.next.prev = node
        prev.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        return node

    def containsKey(self, key):
        if key in self.hash_map:
            return True
        else:
            return False