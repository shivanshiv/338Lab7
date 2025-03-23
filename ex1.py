import random
import time
import matplotlib.pyplot as plt

# =========================================================================
# 1. Implement a binary search tree with insertion and search operations
# ===========================================================================
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        
        balance = self.get_balance(node)
        
        if balance > 1:  # Right heavy
            if key > node.right.key:  # Outside case (3a)
                return self.left_rotate(node)
            else:  # Inside case (3b)
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        
        elif balance < -1:  # Left heavy
            if key < node.left.key:  # Outside case (3a)
                return self.right_rotate(node)
            else:  # Inside case (3b)
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        return node
    
    def search(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

# ==================================================================
# 2. Implement code to measure balance for each node in the tree
# ==================================================================
    def get_balance(self, node):
        if node is None:
            return 0
        return self._height(node.right) - self._height(node.left)
    
    def _height(self, node):
        if node is None:
            return 0
        return node.height
    
    
# ===========================================
# 3. Generate 1000 random search tasks
# ===============================================
bst = BST()
values = list(range(1000))
random.shuffle(values)
for val in values:
    bst.insert(val)

search_tasks = []
for _ in range(1000):
    shuffled = values[:]
    random.shuffle(shuffled)
    search_tasks.append(shuffled)

# =====================================================================
# 4. Measure average performance and largest absolute balance value
# =======================================================================
search_times = []
balance_values = []

for task in search_tasks:
    start_time = time.time()
    for num in task:
        bst.search(num)
    end_time = time.time()
    
    avg_time = (end_time - start_time) / 1000
    search_times.append(avg_time)
    
    # Compute max absolute balance for all nodes in the tree
    def max_abs_balance(node):
        if node is None:
            return 0
        return max(abs(bst.get_balance(node)), max_abs_balance(node.left), max_abs_balance(node.right))
    
    max_balance = max_abs_balance(bst.root)
    balance_values.append(max_balance)

# ============================================================
# 5. Generate scatterplot of absolute balance vs. search time
# ===========================================================
plt.figure(figsize=(10, 6))
plt.scatter(balance_values, search_times, alpha=0.5, c='blue', edgecolors='black')
plt.xlabel("Absolute Balance Factor")
plt.ylabel("Search Time (s)")
plt.title("BST Balance vs Search Performance")
plt.grid(True)
plt.show()
