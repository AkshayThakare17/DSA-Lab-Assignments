class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    else:
        print("Duplicate value not inserted.")
    return root


def inorder_non_recursive(root):
    stack = []
    current = root
    while current is not None or len(stack) > 0:
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
    while len(stack) > 0:
        current = stack.pop()
        print(current.data, end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)


root = None
n = int(input("Enter number of nodes: "))
for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)

print("\nNon-Recursive Inorder Traversal  : ", end="")
inorder_non_recursive(root)
print("\nNon-Recursive Preorder Traversal : ", end="")
preorder_non_recursive(root)
print()
