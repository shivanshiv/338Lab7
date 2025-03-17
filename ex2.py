# ENSF 338 Lab 7 Exercise 2

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.balance = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            print("Inserted root node:", key)
            return
        
        pivot = None
        self.root, pivot = self._insert(self.root, key)
        
        # 2) Code that identifies case 1
        if pivot is None:
            print("Case #1: Pivot not detected")
            
        # 3) Code that identifies case 2
        elif pivot:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        # 4) Code that identifies case 3
        else:
            print("Case #3 not supported")
            
    # 1) Implementing code to identify the pivot node on node insertion
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key), None
        
        if key < node.val:
            node.left, pivot = self._insert(node.left, key)
            if node.left:
                node.balance -= 1
        else:
            node.right, pivot = self._insert(node.right, key)
            if node.right:
                node.balance += 1
        
        if abs(node.balance) > 1:
            pivot = node
        
        return node, pivot

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.print_tree(node.left, level + 1)

# Test Cases
def test_cases():
    bst = BST()
    
    # Test Case 1
    print("Test Case 1:")
    bst.insert(10)
    bst.insert(20)
    bst.insert(30)
    bst.print_tree(bst.root)
    
    # Test Case 2
    print("\nTest Case 2:")
    bst2 = BST()
    bst2.insert(10)
    bst2.insert(5)
    bst2.insert(15)
    bst2.insert(3)
    bst2.print_tree(bst2.root)
    
    # Test Case 3
    print("\nTest Case 3:")
    bst3 = BST()
    bst3.insert(10)
    bst3.insert(20)
    bst3.insert(30)
    bst3.insert(25)
    bst3.print_tree(bst3.root)

    # Test Case 4
    print("\nTest Case 4:")
    bst4 = BST()
    bst4.insert(30)
    bst4.insert(20)
    bst4.insert(10)
    bst4.print_tree(bst4.root)

test_cases()
