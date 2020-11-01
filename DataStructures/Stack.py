class Stack:
    def __init__(self, limit=float("inf"), stack_type=None):
        self.stack = []
        self.limit = limit
        self.stack_type = stack_type

    def __str__(self):
        return str(self.stack)

    def push(self, elem):
        if len(self.stack) == self.limit:
            raise IndexError("Stack is full")
        elif self.stack_type is not None and type(elem) is not self.stack_type:
            raise ValueError("Attempted to push a {} in a {} stack".format(type(elem), self.stack_type))
        else:
            self.stack.append(elem)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")

        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")

        return self.stack[-1]


def __main__():
    stack = Stack()
    stack.push(3)
    print(stack)

    stack.push(4)
    print(stack)

    stack.push("Hello")
    print(stack)

    print("pop", stack.pop())
    print(stack)

    print("peek", stack.peek())
    print(stack)


__main__()
"""
Last in first out Data structure.

Operations:
   - Pop: Pops item from the top of the stack (Yes)
   - Peek: Peeks the top of the stack (Yes)
   - Push: Pushes item on top of stack (Yes)

Basic operations:   
push(3)
[3]

push(4)
[3, 4]

pop() -> return 4
[3]

peek() -> returns 3
[3]

Edge cases:
Is there a limit to how big the stack can be? (Yes)
    - Throw an exception. StackOverflow?
What happens when you attempt to pop an element from an empty stack? (Yes)
    - Throw an exception. EmptyStackException?
What happens when you peek an empty stack? (Yes)
    - Throw an exception. EmptyStackException?
Can more than one thread have this stack at the same time? (Not yet)
    - If so implement some mutexes
    
Other considerations:
What should the to_string be? For example when you call print(stack) -> Should it just print the array?
Are the elements in the array homogenous. Meaning should they all be integers, all be strings etc? (Not yet)
Or can it just have anything.
    - Lets say for now it has to be homogenous

Implementation:
Can us an array or an underlying LinkedList
"""