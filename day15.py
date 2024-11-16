n = int(input('Enter number of Gold coins: '))
coin_values = []

print(f'Enter values of {n} Gold coins')
for i in range(n):
    coin_values.append(int(input()))

q = int(input('Enter number of instructions: '))
instructions = list()

print(f'Enter the {q} instructions')
for i in range(q):
    instructions.append(input().strip().lower())

x = int(input('Enter value of X: '))

monk_stack = []
condition_met = False

print(coin_values, '\n', instructions)

j = 0
for i in range(0, q):
    if instructions[i] == 'harry' and i < len(coin_values):
        monk_stack.append(coin_values[j])
        j += 1
    elif instructions[i] == 'remove':
        monk_stack.pop()
    if sum(monk_stack) == x:
        condition_met = True
        break #break the loop

if condition_met:
    print(f'Number of coins = {len(monk_stack)}')
else:
    print('-1')

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
m = int(input('Enter value of m: '))

a_power_b = a ** b

remainder = a_power_b - m * (a_power_b // m)

print(f'Remainder = {remainder}')

n = int(input('Enter number of test cases: '))

prime_numbers = []

print(f'Enter {n} number of PRime numbers')
for i in range(n):
    prime_numbers.append(int(input()))

for i in range(n):
    if prime_numbers[i] == 2:
        print('0 0')
    elif prime_numbers[i] == 3:
        print('1 0')
    elif prime_numbers[i] == 5:
        print('1 1')
    elif prime_numbers[i] == 7:
        print('0 1')

import sys

class Node:
    def __init__(self):
        self.left  = None
        self.data  = 0
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self, node_data):
        new_node = Node() # created a new node
        new_node.data = node_data

        if self.root is None:
            self.root = new_node
            return
        
        temp1 = self.root
        temp2 = None

        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def get_height(self, root):
        if root == None:
            return 0 # When tree is empty
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height, right_height) + 1
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end='  ')
        self.inorder(root.right)

def create_tree(bst):
    number_of_nodes = int(input('Enter number of nodes: '))
    node_values = []
    print(f'Enter {number_of_nodes} values of the nodes')
    for i in range(number_of_nodes):
        node_values.append(int(input()))
        bst.add_node(node_values[-1])

def run_app(bst):
    create_tree(bst)
    print('The BST is')
    bst.inorder(bst.root)
    print('\nHeight of the BST is', bst.get_height(bst.root))

bst = BST()
run_app(bst)