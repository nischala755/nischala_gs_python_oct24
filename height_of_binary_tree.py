class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None

def new_node(val):
    return TreeNode(val)

def insert(node, val):
    if node is None:
        return new_node(val)
    if val <= node.x:
        node.L = insert(node.L, val)
    else:
        node.R = insert(node.R, val)
    return node

def height(root):
    if root is None:
        return -1
    else:
        lsth = height(root.L)
        rsth = height(root.R)
        return max(lsth, rsth) + 1

# Input handling and tree building
if __name__ == "__main__":
    N = int(input("Enter the number of nodes: "))  # Input number of nodes
    root = None
    for _ in range(N):
        val = int(input("Enter value: "))  # Input tree node value
        root = insert(root, val)
    
    print("Height of the tree:", height(root))
