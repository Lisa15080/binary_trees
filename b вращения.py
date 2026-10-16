class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def add(root, key):
    if root is None:
        return Node(key)

    current = root

    while True:
        if key == current.key:
            return root

        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root
            current = current.right


def rotate_left(root):
    current = root.right
    root.right = current.left
    current.left = root
    return current


def rotate_right(root):
    current = root.left
    root.left = current.right
    current.right = root
    return current


def rotate(root, key, com):
    if key < root.key:
        root.left = rotate(root.left, key, com)
    elif key > root.key:
        root.right = rotate(root.right, key, com)
    else:
        if com == "left":
            return rotate_left(root)
        return rotate_right(root)

    return root


def preorder(root, result):
    if root is None:
        return

    result.append(root.key)
    preorder(root.left, result)
    preorder(root.right, result)

n = int(input())
a = list(map(int, input().split()))

root = None
for key in a:
    root = add(root, key)

m = int(input())

for i in range(m):
    com, key = input().split()
    root = rotate(root, int(key), com)

    result = []
    preorder(root, result)
    print(*result)