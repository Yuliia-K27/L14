class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_list(self, value_list):
        for value in value_list:
            self.add_node(value)

    def add_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right

    def print_tree(self, node=None, level=0):
        if not node:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        if node.left:
            self.print_tree(node.left, level + 1)

my_tree = Tree()
my_tree.add_list([3, 7, 1, 5, 9])
my_tree.print_tree()
