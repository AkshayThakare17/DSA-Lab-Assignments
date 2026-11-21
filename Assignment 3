from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert_node(root.left, value)
    elif value > root.data:
        root.right = insert_node(root.right, value)
    else:
        print("Duplicate Employee ID")
    return root


def copy_tree(root):
    if root is None:
        return None
    new_node = Node(root.data)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)
    return new_node


def level_order(root):
    if root is None:
        print("Tree is Empty")
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    print()


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)


root = None
copy_root = None
choice = 0

while choice != 7:
    print("\n=====================================")
    print(" Employee Database Analysis using BST")
    print("=====================================")
    print("1. Insert Employee IDs")
    print("2. Display Original BST (Level Order)")
    print("3. Copy BST")
    print("4. Display Copied BST (Level Order)")
    print("5. Find Height of BST")
    print("6. Display Leaf Nodes")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of employee IDs: "))
        for i in range(1, n + 1):
            value = int(input(f"Enter Employee ID {i}: "))
            root = insert_node(root, value)
    elif choice == 2:
        print("Original BST (Level Order): ", end="")
        level_order(root)
    elif choice == 3:
        copy_root = copy_tree(root)
        print("BST Copied Successfully")
    elif choice == 4:
        print("Copied BST (Level Order): ", end="")
        level_order(copy_root)
    elif choice == 5:
        print("Height of BST =", height(root))
    elif choice == 6:
        print("Leaf Nodes are: ", end="")
        print_leaf_nodes(root)
        print()
    elif choice == 7:
        print("Exiting Program...")
    else:
        print("Invalid Choice")
