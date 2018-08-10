class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.items)

    def peek(self):
        print(len(self.items))
        return self.items[len(self.items) - 1]


myStack = Stack()
myStack.push("My first exercise")
print("Peeked item is", myStack.peek())
myStack.push(1)
print("Peeked item is", myStack.peek())
print("just popped", myStack.pop())
print("Is the stack empty %s " % (myStack.is_empty()))
print("just popped again", myStack.pop())
if not myStack.is_empty():
    print("Peeked item is", myStack.peek())
else:
    print("stack is empty")

'''
Code to find if there are balanced parenthesis
'''


def check_for_balanced_braces():
    input_string = input("Please enter the string of braces")
    for c in input_string:
        if c == '(':
            myStack.push(c)
        else:
            if not myStack.is_empty():
                myStack.pop()
            else:
                print("Brackets are not balanced")
                return

    if myStack.size() == 0:
        print("Brackets are balanced")
    else:
        print("Brackets are not balanced")


check_for_balanced_braces()
