class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.book, end=" -> ")
            temp = temp.next

        print("None")


library = LinkedList()

library.insert_beginning("Python")
library.insert_beginning("C++")
library.insert_end("Data Structures")

library.display()

library.delete_beginning()

library.display()
