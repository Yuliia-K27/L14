class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
            return

        curr_node = self.root
        while curr_node:
            if data < curr_node.data:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(data)
                    break
            elif data > curr_node.data:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(data)
                    break
            else:
                # data is already in the tree
                break

 #Додамо до класу Tree методи пошуку мінімального і максимального значення елементів в бінарному дереві пошуку:              
    def add_list(self, data_list):
        for data in data_list:
            self.add_node(data)
            
    def find_min(self):
        if not self.root:
            return None

        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left

        return curr_node.data

    def find_max(self):
        if not self.root:
            return None

        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.data
            
