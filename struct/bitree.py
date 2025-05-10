class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None: 
            self.root = Node(key)
        else:  
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
    
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)


bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(50)

print(bst.search(30))
print(bst.search(90))