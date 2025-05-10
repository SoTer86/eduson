class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    
    return root

    
def create_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root
    

root = create_tree()

root = insert_node(root, 8)
print(root.left)

