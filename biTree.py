class Node(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild

class Tree(object):
    def __init__(self):
        self.root=Node()
        self.myQueue=[]
        
    def add(self,elem):
        node=Node(elem)
        if self.root.elem==-1:#根-1
            self.root=node
            self.myQueue.append(self.root)
        else:
            treeNode=self.myQueue[0]
            if treeNode.lchild==None:
                treeNode.lchild=node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild=node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)
    
    def middle_digui(self,root):
        if root==None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)
        
    def lvl_queue(self,root):
        if root==None:
            return
        myQueue=[]
        node=root
        myQueue.append(node)
        while myQueue:
            node=myQueue.pop(0)
            print(node.elem)
            if node.lchild!=None:
                myQueue.append(node.lchild)
            if node.rchild!=None:
                myQueue.append(node.rchild)
                

if __name__=='__main__':
    print(-1)
    elems=range(10)
    tree=Tree()
    for elem in elems:
        tree.add(elem)
    print('next')
    tree.middle_digui(tree.root)
    print('next')
    tree.lvl_queue(tree.root)
    
