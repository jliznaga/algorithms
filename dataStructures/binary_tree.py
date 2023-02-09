class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    #  LEFT -> ROOT -> RIGHT
    def inorder_traversal(self, root):
        nodes = []
        if root:
            nodes = self.inorder_traversal(root.left)
            nodes.append(root.data)
            nodes += self.inorder_traversal(root.right)
        return nodes

    #  ROOT -> LEFT -> RIGHT / DFS (Depth-First Search)
    def preorder_traversal(self, root):
        nodes = []
        if root:
            nodes.append(root.data)
            nodes += self.preorder_traversal(root.left)
            nodes += self.preorder_traversal(root.right)
        return nodes

    #  LEFT -> RIGHT -> ROOT
    def postorder_traversal(self, root):
        nodes = []
        if root:
            nodes = self.postorder_traversal(root.left)
            nodes += self.postorder_traversal(root.right)
            nodes.append(root.data)
        return nodes

    def find_value(self, value):
        if value < self.data:
            if self.left is None:
                return f"{value} is not Found"
            return self.left.find_value(value)
        elif value > self.data:
            if self.right is None:
                return f"{value} is not Found"
            return self.right.find_value(value)
        return f"Value {value} is found"
