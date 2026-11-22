class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, name):
        if self.count == self.size:
            print("Queue is full. No more tickets can be booked.")
            return
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = name
        self.count += 1
        print(name, "joined the queue.")

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty.")
            return
        name = self.arr[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        print(name, "got the ticket and left the queue.")

    def display(self):
        if self.count == 0:
            print("Queue is empty.")
            return
        print("People in queue (front to rear):")
        i = self.front
        for _ in range(self.count):
            print(self.arr[i], end="  ")
            i = (i + 1) % self.size
        print()


q = Queue(4)
choice = 0
while choice != 4:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter customer name: ")
        q.enqueue(name)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        print("Exiting program.")
    else:
        print("Invalid choice.")
