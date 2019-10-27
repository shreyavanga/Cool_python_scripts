class node(object):

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

class binary_search_tree(object):

    def __init__(self):
        self.root=None

    def insert_node(self,data):
        new_node=node.node(data)
        if self.root==None:
            self.root=new_node
        else:
            current_node=self.root
            while True:
                if data<current_node.data:
                    if current_node.leftchild==None:
                        current_node.leftchild=new_node
                        break
                    else:
                        current_node=current_node.leftchild
                elif data>current_node.data:
                    if current_node.rightchild==None:
                        current_node.rightchild=new_node
                        break
                    else:
                        current_node=current_node.rightchild
    def _insertL(self,arr,root,i, n):
        if i < n:
            if arr[i] != -1 :
                temp = node(arr[i])
                root = temp
                root.leftchild = self._insertL(arr, root.leftchild,2 * i + 1, n)
                root.rightchild = self._insertL(arr, root.rightchild,2 * i + 2, n)

    def insertL(self,arr,i,n):
        self._insertL(arr,self.root,i,n)





    def preorder(self,root):
        if root ==None :
            return
        else:

            print(root.data,end="--")
            self.preorder(root.leftchild)
            self.preorder(root.rightchild)

n=input()
v=n.split(" ")
arr=[]
for i in v:
    temp=int(i)
    arr.append(temp)
bst=binary_search_tree();
bst.insertL(arr,0,len(arr))
print(bst.preorder(bst.root))


