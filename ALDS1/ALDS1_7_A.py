

class node:
    def __init__(self,nodeid):
        self.parent = "" 
        self.child = []
        self.childid = []
        self.parent = -1
        self.parentid = -1
        self.nodeid = nodeid
        self.type = "root"
    def setChild(self,cn):
        self.child.append(cn)
        self.childid.append(cn.nodeid)
        cn.parent = self
        cn.parentid = self.nodeid
        cn.setNodeType()
        self.setNodeType()
        return
    def getDepth(self):
        cnt = 0
        t = self
        while True:
            if (t.parentid == -1 or  cnt > 10):
                break
            t = t.parent
            cnt = cnt + 1
        return cnt
    def getChildCount(self):
        return len(self.child)
    def setNodeType(self):
        if (self.getDepth() == 0):
            self.type = "root"
        else:
            if (len(self.child) == 0 ):
                self.type = "leaf"
            else:
                self.type = "internal node" 
    def getNodeType(self):
        return self.type
    def showNode(self):
        print ('node {}: parent = {}, depth = {}, {}, {}'.format(self.nodeid,self.parentid,self.getDepth(),self.getNodeType(),self.childid))
        return

nl = []
n = int(input())
for i in range(0,n):
    nl.append(node(i))

for i in range(0,n):
    nodeinfo = list (map(int,input().split()))
    for j in nodeinfo[2:]:
        nl[nodeinfo[0]].setChild(nl[j])
for i in range(0,n):
    nl[i].showNode()
