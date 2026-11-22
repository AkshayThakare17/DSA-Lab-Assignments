class Node:
    def __init__(self, roll_no):
        self.roll_no = roll_no
        self.left = None
        self.right = None


def insert(root, roll_no):
    if root is None:
        return Node(roll_no)
    if roll_no < root.roll_no:
        root.left = insert(root.left, roll_no)
    elif roll_no > root.roll_no:
        root.right = insert(root.right, roll_no)
    else:
        print("Duplicate Roll Number. Record not inserted.")
    return root


def inorder_non_recursive(root):
    stack = []
    current = root
    while current is not None or len(stack) > 0:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.roll_no, end=" ")
        current = current.right


def preorder_non_recursive(root):
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        print(current.roll_no, end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


root = None
n = int(input("Enter number of student records: "))
for i in range(1, n + 1):
    roll_no = int(input("Enter roll number " + str(i) + ": "))
    root = insert(root, roll_no)

print("\nStudent Records (Ascending Roll Numbers): ", end="")
inorder_non_recursive(root)
print("\nStudent Records (Backup Order)          : ", end="")
preorder_non_recursive(root)
print()
