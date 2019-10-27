class node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):

    def __init__(self):
        self.root=None
        self.co=0

    def _insertL(self,arr,root,i, n):
        if i < n:
            if arr[i] != -1 :
                self.co = self.co + 1
                print("i=",i,n)
                temp = node(arr[i])
                root = temp
                root.left = self._insertL(arr, root.left,2*i+1,n)
                root.right = self._insertL(arr, root.right,2*i+2,n)
            else:
                self.co+=1
        return root

    def insertL(self,arr,i,n):
        self.root=self._insertL(arr,self.root,i,n)





    def preorder(self,root):
        if root ==None :
            return
        else:

            print(root.data,end="--")
            self.preorder(root.left)
            self.preorder(root.right)
    def printLeft(self,root):
        if root:
            if root.left:
                print(root.data)
                self.printLeft(root.left)
            elif root.right:
                print(root.data)
                self.printLeft(root.right)
    def printRight(self,root):
        if root:
            if root.right:
                self.printRight(root.right)
                print(root.data)
            elif root.left:
                self.printRight(root.left)
                print(root.data)
    def printLeaves(self,root):
        if root:
            self.printLeaves(root.left)
            if not root.left and not root.right:
                print (root.data)
            self.printLeaves(root.right)

    def boundary(self,root):
        self.printLeft(root)
        self.printLeaves(root)
        self.printRight(root.right)


n=input()
v=n.split(" ")
arr=[]
for i in v:
    temp=int(i)
    arr.append(temp)
bst=BST()
print(len(arr))
bst.insertL(arr,0,len(arr))
print(bst.preorder(bst.root))
print(bst.boundary(bst.root))