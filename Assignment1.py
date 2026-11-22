class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, book):
        if len(self.items) == self.size:
            print("Stack is full. Cannot return more books.")
        else:
            self.items.append(book)
            print(book, "returned and placed on the stack.")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty. No books to arrange.")
        else:
            book = self.items.pop()
            print(book, "arranged on the shelf.")

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Top book:", self.items[-1])

    def display(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Books in stack (top to bottom):")
            for i in range(len(self.items) - 1, -1, -1):
                print(self.items[i])


s = Stack(5)
choice = 0
while choice != 5:
    print("\n1.Push (Return Book)  2.Pop (Arrange Book)  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter book name: ")
        s.push(name)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.display()
    elif choice == 5:
        print("Exiting program.")
    else:
        print("Invalid choice.")
