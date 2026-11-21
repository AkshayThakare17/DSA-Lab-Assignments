class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, roll_no):
    if root is None:
        return Node(roll_no)
    if roll_no < root.data:
        root.left = insert(root.left, roll_no)
    elif roll_no > root.data:
        root.right = insert(root.right, roll_no)
    else:
        print("Duplicate Roll Number. Record not inserted.")
    return root


def create_bst():
    root = None
    n = int(input("Enter number of student records: "))
    for i in range(1, n + 1):
        roll_no = int(input(f"Enter roll number {i}: "))
        root = insert(root, roll_no)
    return root


def inorder_non_recursive(root):
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


def preorder_non_recursive(root):
    if root is None:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.data, end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


print("===== Student Admission Records (BST) =====")
root = create_bst()

print("\nStudent Records (Ascending Roll Numbers) - Inorder  : ", end="")
inorder_non_recursive(root)
print("\nStudent Records (Backup Order)           - Preorder : ", end="")
preorder_non_recursive(root)
print()
