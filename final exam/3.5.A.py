"""class node(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left = left
        self.right = right

class tree(object):
    def __init__(self,tree):
        self.root = 0
        self.tree = tree"""


def BFS_Search(tree,t):
    queue=[t]
    depth = len(tree)
    while queue:
        element = queue.pop(0)
        if element*2+1 < depth:
            queue.append(element*2+1)
        if element*2+2 < depth:
            queue.append(element*2+2)
        print(tree[element],end = " ")
def test():
    tree = [0,1,2,3,4,5,6]
    t = 2
    BFS_Search(tree,t)

if __name__ == "__main__":
    test()

