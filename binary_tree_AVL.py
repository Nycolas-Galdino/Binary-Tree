import contextlib
import os
from platform import platform
from random import randint

# The code block is attempting to import the `init` function from the `colorama` module. If the import
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
    def __init__(self, key = None, left = None, right = None, height = 0):
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
        if value.key == tree.key: print("Valor já inserido na árvore")

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
        if value == tree.key: print("\033[1;32mValor encontrado na árvore binária\033[0m")

        elif value < tree.key:
            if tree.left: tree.search_node(tree.left, value)
            else: print("\033[1;31mValor não encontrado na árvore binária\033[0m")

        elif value > tree.key:
            if tree.right: tree.search_node(tree.right, value)
            else: print("\033[1;31mValor não encontrado na árvore binária\033[0m")


    def remove_node(self, tree, value):
        pass

while True:
    try:
        value = float(input("\033[1;36mVamos iniciar a árvore! \n \n Qual será o número raiz?\033[0m \n-> "))
        tree = Tree(value)
        break
    except Exception:
        print('Valor não suportado, digite apenas números.')

while True:
    print("""\n
\033[1;4;36mEscolha uma alternativa:\033[0m
    1 - Inserir valor
    2 - Ver lista pre-order
    3 - Ver lista in_order
    4 - Ver lista pos-order
    
    5 - Visualizar árvore binária
    
    7 - Procurar valor na Lista
    
    8 - Limpar terminal
    9 - Resetar árvore
    
    10 - Inserir números aleatórios
    
    0 - sair""")

    choise = input('-> ')


    try:
        if choise == "0":
            quit()

        elif choise == "1":
            value = float(input("Qual valor você quer escolher? \n-> ").replace(',', '.'))
            tree_value = Tree(value)
            tree.insert_node(tree, tree_value)

        elif choise == "2":
            tree.pre_order(tree)

        elif choise == "3":
            tree.in_order(tree)

        elif choise == "4":
            tree.post_order(tree)

        elif choise == '5':
            tree.print_tree()

        elif choise == "7":
            value = float(input("Qual valor você deseja procurar?"))
            tree.search_node(tree, value)

        elif choise == "8":
            os.system('cls' if 'Windows' in platform() else 'clear')
            print("\033[1;32mTerminal limpo!\033[0m")

        elif choise == "9":
            while True:
                value = float(input("Ok! Qual será o número raiz? -> ").replace(',', '.'))
                tree = Tree(value)
                break
            
        elif choise == "10":
            temp_list = []
            qtd = int(input("Quantas números aleatórios você quer inserir no banco?"))
            for _ in range(qtd):
                tree_value = Tree(randint(0,1000))
                tree.insert_node(tree, tree_value)

        else:
            print('\033[1;31mvalor não reconhecido, digite apenas os números')
    
    except Exception as e:
        print(e)
        print('\033[1;31mValor não suportado, digite apenas números.\033[0m')


