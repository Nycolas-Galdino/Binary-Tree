import os
from platform import platform
from random import randint
import contextlib

# The code block attempts to import the `init` function from the `colorama` module. If the import
# is successful, the `init` function is called. If the import fails, an exception is raised and
# caught. In the exception block, the code uses the `os.system` function to execute the command `pip
# install colorama` to install the `colorama` module. After the installation, the `init` function is
# imported again and called. This ensures that the `colorama` module is installed and initialized
# before proceeding with the rest of the code.
try:
    from colorama import init
    init()
except Exception:
    with contextlib.suppress(Exception):
        os.system('pip install colorama')
        os.system('cls' if 'Windows' in platform() else 'clear')
        from colorama import init
        init()

# The `Tree` class represents a binary tree and provides methods for inserting values into the tree
# and performing different types of tree traversals.
class Tree:
    def __init__(self, key = None, left = None, right = None):
        """
        The function is a constructor for a binary tree node, with optional parameters for the key, left
        child, and right child.
        
        :param key: The key parameter represents the value of the node. It can be any data type, such as an
        integer, string, or object
        :param left: The `left` parameter is used to store the reference to the left child of a node in a
        binary tree
        :param right: The `right` parameter is used to store the reference to the right child node of a
        binary tree node
        """
        self.key = key
        self.left = left
        self.right = right


    def insert_node(self, tree, value):
        """
        The function inserts a value into a binary tree.
        
        :param tree: The parameter "tree" represents the current node in the binary search tree where the
        value is being inserted
        :param value: The "value" parameter represents the value that you want to insert into the tree. It
        is assumed to have a "key" attribute that is used to determine the position of the value in the tree
        """
        if tree.key is None: tree = value
        if value.key == tree.key: print("Value already inserted in the tree")

        elif value.key < tree.key:
            if tree.left:
                tree.insert_node(tree.left, value)
            else:
                tree.left = value

        elif tree.right:
            tree.insert_node(tree.right, value)

        else:
            tree.right = value
            
    def print_tree(self, level=0, prefix="Root: "):
        if self.key is not None:
            print(" " * (level * 4) + prefix + str(self.key))
            if self.left:
                self.left.print_tree(level + 1, f"{level} L--- ")
            if self.right:
                self.right.print_tree(level + 1, f"{level} R--- ")
                    
                    
    def height(self):
        if self.key is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1

    def print_tree_2(self):
        tree_height = self.height()
        if tree_height == 0:
            return

        nodes = [self]
        level = 1

        while nodes and level <= tree_height:
            nodes_count = len(nodes)
            space = 2 ** (tree_height - level + 1) - 1
            print(' ' * (space // 2), end='')

            new_nodes = []
            for node in nodes:
                if node is not None:
                    print(node.key, end='')
                    new_nodes.extend(
                        (
                            node.left or None,
                            node.right or None,
                        )
                    )
                else:
                    print(' ', end='')

                print(' ' * space, end='')
            print()
            nodes = new_nodes
            level += 1

    
    def pre_order(self, tree):
        """
        The pre_order function prints the key of each node in a binary tree in pre-order traversal.
        
        :param tree: The parameter `tree` represents the root node of a binary tree
        :return: The function is not explicitly returning anything. If the condition `if not self.key` is
        true, then the function will return `None` by default. Otherwise, the function will print the key of
        the tree and recursively call `pre_order` on the left and right subtrees.
        """
        if not self.key: return

        print(tree.key)
        if tree.left: self.in_order(tree.left)
        if tree.right: self.in_order(tree.right)


    def in_order(self, tree):
        """
        The function recursively prints the keys of a binary tree in ascending order.
        
        :param tree: The parameter "tree" represents a node in a binary tree
        :return: The function does not explicitly return anything. If the tree is empty (self.key is None),
        the function will return None. Otherwise, it will recursively traverse the tree and print the keys
        in order.
        """
        if not self.key: return

        if tree.left: self.in_order(tree.left)
        print(tree.key)
        if tree.right: self.in_order(tree.right)


    def post_order(self, tree):
        """
        The function performs a post-order traversal of a binary tree and prints the keys of the nodes.
        
        :param tree: The parameter `tree` represents a node in a binary tree
        :return: The function does not explicitly return anything. If the condition `if not self.key` is
        true, then the function will return `None` by default.
        """
        if not self.key: return

        if tree.left: self.in_order(tree.left)
        if tree.right: self.in_order(tree.right)
        print(tree.key)


    def search_node(self, tree, value):
        if value == tree.key: print("\033[1;32mValue found in the binary tree\033[0m")

        elif value < tree.key:
            if tree.left: tree.search_node(tree.left, value)
            else: print("\033[1;31mValue not found in the binary tree\033[0m")

        elif value > tree.key:
            if tree.right: tree.search_node(tree.right, value)
            else: print("\033[1;31mValue not found in the binary tree\033[0m")


    def remove_node(self, tree, value):
        if tree.key is None:  #Caso não tenha uma raiz
            print("The value was not found in the tree")
            return None

        else:
            print(tree.key, tree.left, tree.right, tree.key==value)
            if tree.key == value:
                if tree.left is None and tree.right is None: #Remover nó com na folha
                    tree.key = None
                    print(f'The value {value} was removed from the tree')

                elif tree.left != None and tree.right != None:  #Remover nó com 2 filhos
                    temp_key = tree.key
                    temp_node_r = tree.left
                    
                    while temp_node_r.right != None:
                        temp_node_r = temp_node_r.right

                    tree.key = temp_node_r.key
                    temp_node_r.key = temp_key
                    tree.remove_node(tree.left, value)

                elif tree.left != None: #Remover nó com 1 filhos
                    print(1)
                    tree = tree.left

                elif tree.right != None: #Remover nó com 1 filhos
                    print(2)
                    tree = tree.right


            elif tree.key < value:
                if tree.right is None: 
                    print("The value was not found in the tree")
                    return None
                tree.remove_node(tree.right, value)

            elif tree.key > value:
                if tree.left is None: 
                    print("The value was not found in the tree")
                    return None
                tree.remove_node(tree.left, value)

while True:
    try:
        value = float(input("\033[1;36mLet's start the tree! \n \n What will be the root number?\033[0m \n-> "))
        tree = Tree(value)
        break
    except Exception:
        print('Unsupported value, please input only numbers.')

while True:
    print("""\n
\033[1;4;36mChoose an option:\033[0m
    1 - Insert value
    2 - View pre-order list
    3 - View in-order list
    4 - View post-order list
    
    5 - Remove value
    
    6 - Visualize binary tree
    
    7 - Search value in the List
    
    8 - Clear terminal
    9 - Reset tree
    
    10 - Insert random numbers
    
    0 - Exit""")

    choise = input('-> ')


    try:
        if choise == "0":
            quit()

        elif choise == "1":
            value = float(input("Which value do you want to insert? \n-> ").replace(',', '.'))
            tree_value = Tree(value)
            tree.insert_node(tree, tree_value)

        elif choise == "2":
            tree.pre_order(tree)

        elif choise == "3":
            tree.in_order(tree)

        elif choise == "4":
            tree.post_order(tree)

        elif choise == '5':
            value = int(input("Ok! What will be the root removed? \n-> ").strip())
            tree.remove_node(tree, value)

        elif choise == '6':
            tree.print_tree()

        elif choise == "7":
            value = float(input("What value are you looking for? \n-> "))
            tree.search_node(tree, value)

        elif choise == "8":
            os.system('cls' if 'Windows' in platform() else 'clear')
            print("\033[1;32mTerminal cleaned!\033[0m")

        elif choise == "9":
            while True:
                value = float(input("Ok! What will be the new root number? -> ").replace(',', '.'))
                tree = Tree(value)
                break
            
        elif choise == "10":
            temp_list = []
            qtd = int(input("How many random numbers do you want to insert into the tree?"))
            for _ in range(qtd):
                tree_value = Tree(randint(0,1000))
                tree.insert_node(tree, tree_value)

        else:
            print('\033[1;31mValue not recognized, please input only numbers')
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        print('\033[1;31mUnsupported value, please input only numbers.\033[0m')
