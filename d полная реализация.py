class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(root):
    if root is None:
        return 0
    return root.height


def update(root):
    root.height = 1 + max(height(root.left), height(root.right))


def balance_factor(root):
    return height(root.right) - height(root.left)


def rotate_left(root):
    current = root.right
    root.right = current.left
    current.left = root

    update(root)
    update(current)
    return current


def rotate_right(root):
    current = root.left
    root.left = current.right
    current.right = root

    update(root)
    update(current)
    return current


def fix(root):
    update(root)
    bal = balance_factor(root)

    if bal == 2:
        if balance_factor(root.right) < 0:
            root.right = rotate_right(root.right)
        return rotate_left(root)

    if bal == -2:
        if balance_factor(root.left) > 0:
            root.left = rotate_left(root.left)
        return rotate_right(root)

    return root


def add(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = add(root.left, key)
    elif key > root.key:
        root.right = add(root.right, key)
    else:
        return root

    return fix(root)


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
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        succ = find_min(root.right)
        root.key = succ.key
        root.right = delete(root.right, succ.key)

    return fix(root)


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


def next(root, key):
    current = root
    result = None

    while current is not None:
        if current.key >= key:
            result = current.key
            current = current.left
        else:
            current = current.right

    return result


def prev(root, key):
    current = root
    result = None

    while current is not None:
        if current.key <= key:
            result = current.key
            current = current.right
        else:
            current = current.left

    return result


def preorder(root, result):
    if root is None:
        return

    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)

root = None
q = int(input())
ans = []

for i in range(q):
    com = input().split()

    if com[0] == "add":
        root = add(root, int(com[1]))

    elif com[0] == "del":
        root = delete(root, int(com[1]))

    elif com[0] == "exists":
        if exists(root, int(com[1])):
            ans.append("YES")
        else:
            ans.append("NO")

    elif com[0] == "next":
        ans.append(str(next(root, int(com[1]))))

    elif com[0] == "prev":
        ans.append(str(prev(root, int(com[1]))))

    elif com[0] == "root":
        if root is None:
            ans.append("Empty")
        else:
            ans.append(str(root.key))

    elif com[0] == "height":
        ans.append(str(height(root)))

    elif com[0] == "print":
        result = []
        preorder(root, result)

        if result:
            ans.append(" ".join(result))
        else:
            ans.append("Empty")

for s in ans:
    print(s)
