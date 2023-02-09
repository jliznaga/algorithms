
class Node:
    def __init__(self, nextval=None, dataval=None):
        self.dataval = dataval
        self.nextval = nextval

    def __str__(self) -> str:
        self.dataval


array = []
n = None
for i in range(1, 11):
    node = Node(n, i)
    array.append(node)
    n = node


def center_node(arg):
    arr = []
    next = arg.nextval
    while (next is not None):
        arr.append(next)

    ln = len(arr)
    index = ln//2
    return arr[index].dataval


assert center_node(n) == ''
