class Stack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return "Stack is empty"

    def display(self):
        if self.stack:
            print("Books:", self.stack)
        else:
            print("Stack is empty")


s = Stack()

s.push("Python")
s.push("Data Structures")
s.push("Database")

s.display()
print("Top Book:", s.peek())
print("Arrange Book:", s.pop())
s.display()
