class AVLNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, book):
        if not root:
            return AVLNode(book)
        if book['rating'] < root.book['rating']:
            root.left = self.insert(root.left, book)
        elif book['rating'] > root.book['rating']:
            root.right = self.insert(root.right, book)
        else:
            return root

        self.update_height(root)
        balance = self.balance_factor(root)

        # left left
        if balance > 1 and book['rating'] < root.left.book['rating']:
            return self.right_rotate(root)

        # right right
        if balance < -1 and book['rating'] > root.right.book['rating']:
            return self.left_rotate(root)

        # left right
        if balance > 1 and book['rating'] > root.left.book['rating']:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # right left
        if balance < -1 and book['rating'] < root.right.book['rating']:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_book(self, book):
        self.root = self.insert(self.root, book)

    def inorder_traversal(self, root, books):
        if not root:
            return
        self.inorder_traversal(root.left, books)
        books.append(root.book)
        self.inorder_traversal(root.right, books)
