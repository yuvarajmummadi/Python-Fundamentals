class Node:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root = None
    def insert(self,data):
        self.root = self.rec_insert(self.root,data)
    def rec_insert(self,root,data):
        if root is None:
            return Node(data)
        if root.data >data:
            root.left = self.rec_insert(root.left,data)
        else:
            root.right = self.rec_insert(root.right,data)
        return root
    def inorder(self):
        def rec_inorder(root):
            if root:
                rec_inorder(root.left)
                print(root.data,end=" ")
                rec_inorder(root.right)
        rec_inorder(self.root)
    def count(self,root):
        if not root:
            return 0
        return 1+max(self.count(root.left),self.count(root.right))
    def sum(self,root):
        if not root:
            return 0
        return root.data+self.sum(root.left)+self.sum(root.right)
obj = bst()
obj.insert(25)
obj.insert(63)
obj.insert(72)
obj.insert(22)
obj.insert(35)
obj.insert(17)
obj.inorder()
print()
print(obj.count(obj.root))
print(obj.sum(obj.root))
