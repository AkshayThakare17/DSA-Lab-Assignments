class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None


def insert(root, roll_no, name):
    if root is None:
        return Student(roll_no, name)

    if roll_no < root.roll_no:
        root.left = insert(root.left, roll_no, name)
    else:
        root.right = insert(root.right, roll_no, name)

    return root


def inorder(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.roll_no, current.name)
        current = current.right


def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.roll_no, current.name)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


root = None

root = insert(root, 103, "Akshay")
root = insert(root, 101, "Rahul")
root = insert(root, 105, "Priya")
root = insert(root, 102, "Amit")
root = insert(root, 104, "Sneha")

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)
