# https://www.hackerrank.com/domains/data-structures?filters%5Bstatus%5D%5B%5D=unsolved

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        currNode = self.root
        if not currNode:
            self.root = Node(val)
            return self.root
        
        while currNode:
            if currNode.info > val:
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = Node(val)
                    break
            else:
                if currNode.right:
                    currNode = currNode.right
                else:
                    currNode.right = Node(val)
                    break
        
        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
