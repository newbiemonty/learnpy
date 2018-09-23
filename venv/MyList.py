class Node:
    def __init__(self, init_val):
        self.data = init_val
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def length(self):
        return self.count

    def pop(self):
        assert self.tail is not None
        return tail.
    def

    def append(self, val):
        if self.head is None:
            assert self.tail is None
            self.head = Node(val)
            self.tail = self.head
        else:
            assert self.tail is not None
            temp = Node(val)
            self.tail.set_next(temp)
            self.tail = temp

        self.count += 1

    def insert(self, val, pos):
        if self.head is None:
            assert pos == 0
            self.head = Node(val)
            self.tail = self.head
        else:
            assert pos < self.count;
            if pos is 0:
                temp = self.head;
                self.head = Node(val)
                self.head.next = temp;
            else:
                prev = None
                current = self.head
                while pos and current is not None:
                    prev = current
                    current = current.next
                    pos -= 1

        self.count += 1











