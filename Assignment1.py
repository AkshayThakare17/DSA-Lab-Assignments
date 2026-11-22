class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(prompt):
    category = input(prompt).strip()
    if category == "NULL":
        return None
    node = Node(category)
    node.left = create_tree(f"Enter left subcategory of {category}: ")
    node.right = create_tree(f"Enter right subcategory of {category}: ")
    return node


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


print("===== Create Library Catalog (Binary Tree) =====")
print("Enter NULL if a subcategory/book does not exist.")
root = create_tree("Enter root category: ")

print("\nBook Categories (Inorder)       : ", end="")
inorder(root)
print("\nCatalog Structure (Preorder)    : ", end="")
preorder(root)
print("\nArchive/Delete Order (Postorder): ", end="")
postorder(root)
print()
