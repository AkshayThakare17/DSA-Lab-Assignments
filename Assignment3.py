class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(data, "inserted at beginning.")

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print(data, "inserted at end.")

    def delete_beginning(self):
        if self.head is None:
            print("List is empty.")
        else:
            print(self.head.data, "deleted from beginning.")
            self.head = self.head.next

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


catalog = LinkedList()
choice = 0
while choice != 5:
    print("\n1.Insert at beginning  2.Insert at end  3.Delete from beginning  4.Display  5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        catalog.insert_beginning(input("Enter book name: "))
    elif choice == 2:
        catalog.insert_end(input("Enter book name: "))
    elif choice == 3:
        catalog.delete_beginning()
    elif choice == 4:
        catalog.display()
    elif choice == 5:
        print("Exiting program.")
    else:
        print("Invalid choice.")
