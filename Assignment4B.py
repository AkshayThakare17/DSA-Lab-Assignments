class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    category = input("Enter category/book name (NULL for none): ")
    if category == "NULL":
        return None
    node = Node(category)
    print("Enter left subcategory of", category)
    node.left = create_tree()
    print("Enter right subcategory of", category)
    node.right = create_tree()
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


print("Create Library Catalog")
print("Enter root category")
root = create_tree()

print("\nBook Categories (Inorder)        : ", end="")
inorder(root)
print("\nCatalog Structure (Preorder)     : ", end="")
preorder(root)
print("\nArchive/Delete Order (Postorder) : ", end="")
postorder(root)
print()
