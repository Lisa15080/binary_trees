import sys

sys.setrecursionlimit(5000)

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


def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current


def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
        return root

    if key > root.key:
        root.right = delete(root.right, key)
        return root

    if root.left is None:
        return root.right

    if root.right is None:
        return root.left

    succ = find_min(root.right)
    root.key = succ.key
    root.right = delete(root.right, succ.key)

    return root


def exists(root, key):
    current = root

    while current is not None:
        if key == current.key:
            return True

        if key < current.key:
            current = current.left
        else:
            current = current.right

    return False


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def preorder(root, result):
    if root is None:
        return

    result.append(root.key)
    preorder(root.left, result)
    preorder(root.right, result)

root = None
q = int(input())

for i in range(q):
    com = input().split()

    if com[0] == "add":
        root = add(root, int(com[1]))

    elif com[0] == "del":
        root = delete(root, int(com[1]))

    elif com[0] == "exists":
        if exists(root, int(com[1])):
            print("YES")
        else:
            print("NO")

    elif com[0] == "height":
        print(height(root))

    elif com[0] == "print":
        result = []
        preorder(root, result)

        if result:
            print(*result)
        else:
            print("Empty")