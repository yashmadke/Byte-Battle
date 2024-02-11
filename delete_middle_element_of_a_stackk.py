class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()

    def empty(self):
        return len(self.items) == 0

def delete_middle(stack, n, current):
    # if stack is empty or we have reached the end of the stack
    if current == n:
        return

    # Get the current element from the stack
    x = stack.pop()

    # If the current element is not the middle element, push it back to the stack
    if current != n // 2:
        delete_middle(stack, n, current + 1)
        stack.push(x)

# Function to delete the middle element of the stack
def delete_middle_element(stack):
    n = len(stack.items)
    delete_middle(stack, n, 0)


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

delete_middle_element(stack1)
print("Stack after deleting middle element:", stack1.items)

stack2 = Stack()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
stack2.push(5)
stack2.push(6)

delete_middle_element(stack2)
print("Stack after deleting middle element:", stack2.items)