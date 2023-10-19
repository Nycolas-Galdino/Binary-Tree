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


    def insert(self, tree, value):
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
                tree.insert(tree.left, value)
            else:
                tree.left = value

        elif tree.right:
            tree.insert(tree.right, value)

        else:
            tree.right = value


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


while True:
    try:
        value = float(input("Vamos iniciar a árvore! Qual será o número raiz? -> "))
        tree = Tree(value)
        break
    except Exception:
        print('Valor não suportado, digite apenas números.')

while True:
    print("""\n
\033[1;4;31mEscolha uma alternativa:\033[0m
    1 - Inserir valor
    2 - Ver lista pre-order
    3 - Ver lista in_order
    4 - Ver lista pos-order
    
    9 - Resetar árvore
    0 - sair""")

    choise = input('-> ')

    if choise == "0":
        quit()

    elif choise == "1":
        try:
            value = float(input("Qual valor você quer escolher?").replace(',', '.'))
            
            tree_value = Tree(value)
            tree.insert(tree, tree_value)
        except Exception:
            print('Valor não suportado, digite apenas números.')


    elif choise == "2":
        tree.pre_order(tree)

    elif choise == "3":
        tree.in_order(tree)

    elif choise == "4":
        tree.post_order(tree)

    elif choise == "9":
        while True:
            try:
                value = float(input("Ok! Qual será o número raiz? -> ").replace(',', '.'))
                tree = Tree(value)
                break
            except Exception:
                print('Valor não suportado, digite apenas números.')

    else:
        print('valor não reconhecido, digite apenas os números')


