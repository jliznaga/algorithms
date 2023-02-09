class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def insert_after(self, target_data, node: Node):
        if self.head is None:
            raise Exception("Empty List")
        for n in self:
            if n.data == target_data:
                node.next = n.next
                n.next = node
                return
        raise Exception("Node with data '%s' not found" % target_data)

    def insert_before(self, target_data, node: Node):
        if self.head is None:
            raise Exception("Empty List")

        if self.head.data == target_data:
            return self.add_first(node)

        previous_node = self.head
        for n in self:
            if n.data == target_data:
                previous_node.next = node
                node.next = n
                return
            previous_node = n

    def remove_node(self, target_data):
        if self.head is None:
            raise Exception("Empty List")

        if self.head.data == target_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for n in self:
            if n.data == target_data:
                previous_node.next = n.next
                return
            previous_node = n

    def find_center_node(self):
        size = len(list(self)) - 1
        center_index = size // 2 if size % 2 == 0 else (size // 2) + 1
        center = self.head
        counter = 0
        while center is not None and center_index != counter:
            center = center.next
            counter += 1

        return center.data


if __name__ == '__main__':
    llist = LinkedList(["a", "b", "c", "d", "e", "f"])
    print(llist.find_center_node())
