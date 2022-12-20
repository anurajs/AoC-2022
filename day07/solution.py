class Node:
    def __init__(self, parent=None, name="root", value=None):
        self.parent = parent
        self.name = name
        self.value = value
        self.children = []

    def set_children(self, children):
        self.children = children

    def set_value(self, value):
        self.value = value

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        NameError()

    def get_parent(self):
        return self.parent


file_name = "puzzle.txt"
with open(file_name) as file:
    root = Node([], "/")
    current = root
    while(line := file.readline().strip()):
        if line.startswith('$ ls'):
            children = []
            while(not (line := file.readline().strip()).startswith('$') and line != ''):
                type_info, name = line.split(' ')
                if type_info.startswith('dir'):
                    children.append(Node(current, name))
                else:
                    children.append(Node(current, name, int(type_info)))
            current.set_children(children)
        if line == '$ cd /':
            current = root
        elif line == '$ cd ..':
            current = current.parent
        elif line.startswith('$ cd'):
            current = current.get_child(line.split(' ')[2])


def traverse_tree(node, sizes):
    if node.value is None:
        value = 0
        for child in node.children:
            value += traverse_tree(child, sizes)
        node.value = value
        sizes.append(value)
        return value
    else:
        return node.value


sizes = []
total = traverse_tree(root, sizes)
below_100k = [x for x in sizes if x < 100000]
deletables = [x for x in sizes if 70000000 - total + x > 30000000]

print('part 1:', sum(below_100k))
print('part 2:', min(deletables))
