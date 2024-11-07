@classmethod
def class_method(cls):
    MyClass.class_var += 1
    return cls.class_var

@staticmethod
def static_method():
    MyClass.class_var += 1
    return f"This is a static method {MyClass.class_var}"
	
@staticmethod
def another_static_method():
    MyClass.class_var += 1
    return f"This is a static method {MyClass.class_var}"
    

    def __init__(self, name = 'mahesh'):
    self.__id = Student.student_id
    self.__name = name
    Student.student_count += 1
    Student.student_id += 1

def get_name(self):
    return self.__name

def get_id(self):
    return self.__id

@classmethod
def get_student_count(cls):
    return Student.student_count
    # return cls.number_of_students

def __str__(self):
    return f'Id={self.__id}, Name={self.__name}'

def __init__(self, name = 'mahesh'):
    self.__id = Student.student_id
    self.__name = name
    Student.student_count += 1
    Student.student_id += 1

def get_name(self):
    return self.__name

def get_id(self):
    return self.__id

@classmethod
def get_student_count(cls):
    return Student.student_count
    # return cls.number_of_students

def __str__(self):
    return f'Id={self.__id}, Name={self.__name}'

def __init__(self, name, designation, salary):
	self.id = Employee.id
	self.name = name
	self.designation = designation
	self.salary = salary
	Employee.id += 1
def __str__(self):
    return f'{self. id}, {self.name}, {self.designation}, {self.salary}'

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)


def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return self._search_recursive(node.left, value)
    return self._search_recursive(node.right, value)

def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Node with one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children
        min_larger_node = self._min_value_node(node.right)
        node.value = min_larger_node.value
        node.right = self._delete_recursive(node.right, min_larger_node.value)
    return node

def _min_value_node(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

def merge_bsts(bst1, bst2):
    list1 = bst_to_list(bst1.root)
    list2 = bst_to_list(bst2.root)
    merged_list = sorted(list1 + list2)
    return sorted_list_to_bst(merged_list)

def bst_to_list(node):
    if not node:
        return []
    return bst_to_list(node.left) + [node.value] + bst_to_list(node.right)

def sorted_list_to_bst(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = sorted_list_to_bst(lst[:mid])
    root.right = sorted_list_to_bst(lst[mid + 1:])
    return root

def merge_bsts(bst1, bst2):
    list1 = bst_to_list(bst1.root)
    list2 = bst_to_list(bst2.root)
    merged_list = sorted(list1 + list2)
    return sorted_list_to_bst(merged_list)

def bst_to_list(node):
    if not node:
        return []
    return bst_to_list(node.left) + [node.value] + bst_to_list(node.right)

def sorted_list_to_bst(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = sorted_list_to_bst(lst[:mid])
    root.right = sorted_list_to_bst(lst[mid + 1:])
    return root

def balance_bst(bst):
    sorted_list = bst_to_list(bst.root)
    return sorted_list_to _bst(sorted_list)

    class Student:
    pass

class Employee:
    pass

class Manager(Employee):
    pass

class Director(Manager):
    pass

# Example of creating instances
employee = Director()
manager = Director()

student = Student()
employee = Employee()
manager = Manager()

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee))  # True
print(isinstance(employee, Manager))  # False

class Student:
    pass

class Employee:
    pass

class Manager(Employee):
    pass

class Director(Manager):
    pass

# Example of creating instances
employee = Director()
manager = Director()

student = Student()
employee = Employee()
manager = Manager()

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee))  # True
print(isinstance(employee, Manager))  # False

print(issubclass(Director, Employee))  # True
print(issubclass(Manager, Employee))   # True
print(issubclass(Manager, Director))   # False
print(issubclass(Director, Manager))    # True
print(issubclass(Director, Director))   # True

class Student:
    student_count = 0
    student_id = 101

    def __init__(self, name='mahesh'):
        self.__id = Student.student_id
        self.__name = name
        Student.student_count += 1
        Student.student_id += 1

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    @classmethod
    def get_student_count(cls):
        return Student.student_count

    def __str__(self):
        return f'Id={self.__id}, Name={self.__name}'

s1 = Student()
s2 = Student('Girish')
s3 = Student('Satish')

print(s1)  # Calls the implicit method __str__()
print('Student1 name is', s1.get_name())
print('Student1 id is', s1.get_id())
print(getattr(s1, 'branch', 'CSE'))  # To temporarily add a new attribute to the object
print(s1)  # Calls the overridden __str__() method

class Employee:
    id = 101

    def __init__(self, name, designation, salary):
        self.id = Employee.id
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.id += 1

    def __str__(self):
        return f'{self.id}, {self.name}, {self.designation}, {self.salary}'

class Manager(Employee):
    def __init__(self, name, designation, salary, commission):
        super().__init__(name, designation, salary)
        self.commission = commission

    def __str__(self):
        return f'{self.id}, {self.name}, {self.designation}, {self.salary}, {self.commission}'

emp1 = Employee('Asha', 'Developer', 125000)
m1 = Manager('John', 'Manager', 150000, 2500)
emp2 = Employee('Usha', 'Developer', 225000)

print(emp1)
print(m1)
print(emp2)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)


def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return self._search_recursive(node.left, value)
    return self._search_recursive(node.right, value)

def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Node with one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children
        min_larger_node = self._min_value_node(node.right)
        node.value = min_larger_node.value
        node.right = self._delete_recursive(node.right, min_larger_node.value)
    return node

def _min_value_node(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

def merge_bsts(bst1, bst2):
    list1 = bst_to_list(bst1.root)
    list2 = bst_to_list(bst2.root)
    merged_list = sorted(list1 + list2)
    return sorted_list_to_bst(merged_list)

def bst_to_list(node):
    if not node:
        return []
    return bst_to_list(node.left) + [node.value] + bst_to_list(node.right)

def sorted_list_to_bst(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = sorted_list_to_bst(lst[:mid])
    root.right = sorted_list_to_bst(lst[mid + 1:])
    return root

def balance_bst(bst):
    sorted_list = bst_to_list(bst.root return sorted_list_to_bst(sorted_list)

class Student:
    pass

class Employee:
    pass

class Manager(Employee):
    pass

class Director(Manager):
    pass

# Example of creating instances
employee = Director()
manager = Director()

student = Student()
employee = Employee()
manager = Manager()

print(isinstance(manager, Manager))  # True
print(isinstance(manager, Employee))  # True
print(isinstance(employee, Manager))  # False

print(issubclass(Director, Employee))  # True
print(issubclass(Manager, Employee))   # True
print(issubclass(Manager, Director))   # False
print(issubclass(Director, Manager))    # True
print(issubclass(Director, Director))   # True

class Student:
    student_count = 0
    student_id = 101

    def __init__(self, name='mahesh'):
        self.__id = Student.student_id
        self.__name = name
        Student.student_count += 1
        Student.student_id += 1

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    @classmethod
    def get_student_count(cls):
        return Student.student_count

    def __str__(self):
        return f'Id={self.__id}, Name={self.__name}'

s1 = Student()
s2 = Student('Girish')
s3 = Student('Satish')

print(s1)  # Calls the implicit method __str__()
print('Student1 name is', s1.get_name())
print('Student1 id is', s1.get_id())
print(getattr(s1, 'branch', 'CSE'))  # To temporarily add a new attribute to the object
print(s1)  # Calls the overridden __str__() method

class Employee:
    id = 101

    def __init__(self, name, designation, salary):
        self.id = Employee.id
        self.name = name
        self.designation = designation
        self.salary = salary
        Employee.id += 1

    def __str__(self):
        return f'{self.id}, {self.name}, {self.designation}, {self.salary}'

class Manager(Employee):
    def __init__(self, name, designation, salary, commission):
        super().__init__(name, designation, salary)
        self.commission = commission

    def __str__(self):
        return f'{self.id}, {self.name}, {self.designation}, {self.salary}, {self.commission}'

emp1 = Employee('Asha', 'Developer', 125000)
m1 = Manager('John', 'Manager', 150000, 2500)
emp2 = Employee('Usha', 'Developer', 225000)

print(emp1)
print(m1)
print(emp2)
``` ### Algorithms on a Binary Search Tree (BST)

1. **Create a BST (by adding a node)**
   - A BST can be created by defining a class for the nodes and a class for the tree itself. Each node has a value, a left child, and a right child.

   ```python
   class TreeNode:
       def __init__(self, value):
           self.value = value
           self.left = None
           self.right = None

   class BST:
       def __init__(self):
           self.root = None

       def add(self, value):
           if not self.root:
               self.root = TreeNode(value)
           else:
               self._add_recursive(self.root, value)

       def _add_recursive(self, node, value):
           if value < node.value:
               if node.left is None:
                   node.left = TreeNode(value)
               else:
                   self._add_recursive(node.left, value)
           else:
               if node.right is None:
                   node.right = TreeNode(value)
               else:
                   self._add_recursive(node.right, value)

def search(self, value):
    return self._search_recursive(self.root, value)

def _search_recursive(self, node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return self._search_recursive(node.left, value)
    return self._search_recursive(node.right, value)

    def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Node with one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children
        min_larger_node = self._min_value_node(node.right)
        node.value = min_larger_node.value
        node.right = self._delete_recursive(node.right, min_larger_node.value)
    return node

def _min_value_node(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current

    def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

    def merge_bsts(bst1, bst2):
    list1 = bst_to_list(bst1.root)
    list2 = bst_to_list(bst2.root)
    merged_list = sorted(list1 + list2)
    return sorted_list_to_bst(merged_list)

def bst_to_list(node):
    if not node:
        return []
    return bst_to_list(node.left) + [node.value] + bst_to_list(node.right)

def sorted_list_to_bst(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = sorted_list_to_bst(lst[:mid])
    root.right = sorted_list_to_bst(lst[mid + 1:])
    return root

    def balance_bst(bst):
    sorted_list = bst_to_list(bst.root return sorted_list_to_bst(sorted_list)
                              
