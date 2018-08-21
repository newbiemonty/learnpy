class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def push(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

    def detect_cycle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        loop_counter = 0;

        while (slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            if slow_ptr == fast_ptr.next:
                print("looped")
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                print("Cycle detected")
                cycle_detected = True
                break;

        if cycle_detected:
            slow_ptr = self.head
            while slow_ptr == fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next

            print("the loop is at node", slow_ptr.data)








myList = List()

myList.push(1)
myList.push(2)
myList.push(3)
myList.push(4)
myList.push(5)
myList.push(6)
myList.push(8)
myList.push(9)
myList.push(10)
myList.head.next.next.next.next.next.next.next.next.next = myList.head.next.next.next

myList.detect_cycle()

