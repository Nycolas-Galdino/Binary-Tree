import os
import platform
from random import randint

# Try importing colorama, if not available, install it
try:
    import colorama
except ImportError:
    try:
        import subprocess
        subprocess.check_call(['pip', 'install', 'colorama'])
        import colorama
    except Exception as e:
        print("Failed to install colorama:", e)
finally:
    colorama.init()

class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_key=None):
        self.root = TreeNode(root_key)

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Key must be a number")
        
        new_node = TreeNode(key)
        if self.root.key is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key == current.key:
                print("Value already exists in the tree")
                return
            elif key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def pre_order(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.key, end=' ')
            self.in_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.key, end=' ')

    def search(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Key must be a number")

        current = self.root
        while current is not None:
            if key == current.key:
                print("\033[1;32mValue found in the binary tree\033[0m")
                return
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        print("\033[1;31mValue not found in the binary tree\033[0m")

    def print_tree(self):
        levels = self._get_tree_levels()
        for level in levels:
            print(level)

    def _get_tree_levels(self):
        levels = []
        queue = [(self.root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if len(levels) == depth:
                levels.append([])
            if node:
                levels[depth].append(node.key)
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
            else:
                levels[depth].append(None)
        return levels

    def reset_tree(self, root_key=None):
        self.root = TreeNode(root_key)

# Clear the terminal screen
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def input_float(prompt):
    while True:
        try:
            value = float(input(prompt).replace(',', '.'))
            return value
        except ValueError:
            print('Unsupported value, please input only numbers.')

def main():
    tree = None
    while True:
        print("\033[1;36mLet's start the tree!\033[0m")
        root_value = input_float("What will be the root number? -> ")
        tree = BinaryTree(root_value)
        break

    while True:
        print("""\n\033[1;4;36mChoose an option:\033[0m
        1 - Insert value
        2 - View pre-order list
        3 - View in-order list
        4 - View post-order list
        5 - Visualize binary tree
        6 - Search value in the List
        7 - Reset tree
        8 - Insert random numbers
        0 - Exit""")

        choice = input('-> ')

        try:
            if choice == "0":
                quit()

            elif choice == "1":
                value = input_float("Which value do you want to insert? -> ")
                tree.insert(value)

            elif choice == "2":
                print("Pre-order list:", end=' ')
                tree.pre_order(tree.root)
                print()

            elif choice == "3":
                print("In-order list:", end=' ')
                tree.in_order(tree.root)
                print()

            elif choice == "4":
                print("Post-order list:", end=' ')
                tree.post_order(tree.root)
                print()

            elif choice == '5':
                print("Visualizing binary tree:")
                tree.print_tree()

            elif choice == "6":
                value = input_float("Which value do you want to search for? -> ")
                tree.search(value)

            elif choice == "7":
                root_value = input_float("Ok! What will be the new root number? -> ")
                tree.reset_tree(root_value)

            elif choice == "8":
                num_random = int(input("How many random numbers do you want to insert into the tree? -> "))
                for _ in range(num_random):
                    tree.insert(randint(0, 1000))

            else:
                print('\033[1;31mValue not recognized, please input only numbers')

        except ValueError as e:
            print(e)
            print('\033[1;31mUnsupported value, please input only numbers.\033[0m')

        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()
