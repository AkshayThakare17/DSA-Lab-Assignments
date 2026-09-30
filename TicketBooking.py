class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ticket):
        self.queue.append(ticket)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

    def display(self):
        if self.queue:
            print("Tickets:", self.queue)
        else:
            print("Queue is empty")


q = Queue()

q.enqueue("Ticket 101")
q.enqueue("Ticket 102")
q.enqueue("Ticket 103")

q.display()
print("Booked Ticket:", q.dequeue())
q.display()
