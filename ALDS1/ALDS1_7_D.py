# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_D
# Reconstruction of a Tree

import copy
class node:
    def __init__(self,nodeid):
        self.parent = None
        self.parentid = -1
        self.c_leftid = -1
        self.c_left = None
        self.c_rightid = -1
        self.c_right = None
        self.nodeid = nodeid
        self.type = "root"
    def setLeftChild(self,cn):
        self.c_left = cn
        self.c_leftid = cn.nodeid
        cn.parent = self
        cn.parentid = self.nodeid
        cn.setNodeType()
        self.setNodeType()
        return
    def setRightChild(self,cn):
        self.c_right = cn
        self.c_rightid = cn.nodeid
        cn.parent = self
        cn.parentid = self.nodeid
        cn.setNodeType()
        self.setNodeType()
        return
    def getDepth(self):
        cnt = 0
        t = self
        while True:
            if (t.parentid == -1 ):
                break
            t = t.parent
            cnt = cnt + 1
        return cnt
    def setNodeType(self):
        if (self.getDepth() == 0):
            self.type = "root"
        else:
            if ( self.c_rightid == -1 and self.c_leftid == -1 ):
                self.type = "leaf"
            else:
                self.type = "internal node" 
    def getNodeType(self):
        return self.type
    def getSibling(self):
        if ( self.parentid == -1):
            return -1
        i = self.parent
        if ( i.c_rightid == self.nodeid ):
            return i.c_leftid
        elif ( i.c_leftid == self.nodeid):
            return i.c_rightid
    def getHeight(self):
        lcnt = 0
        rcnt = 0
        if (self.c_leftid == -1  and self.c_rightid == -1 ):
            return 0
        elif (self.c_rightid  == -1):
            lcnt = lcnt + self.c_left.getHeight() + 1
        elif (self.c_leftid  == -1):
            rcnt = rcnt + self.c_right.getHeight() + 1
        else:
            lcnt = lcnt + self.c_left.getHeight() + 1
            rcnt = rcnt + self.c_right.getHeight() + 1
        if (lcnt >= rcnt):
            return lcnt
        else:
            return rcnt
    def getDegree(self):
        cnt = 0
        if (self.c_leftid != -1):
            cnt += 1
        if (self.c_rightid != -1):
            cnt += 1
        return cnt
    def getPreorder(self,r1):
        r1.append(self.nodeid)
        if (self.c_leftid != -1):
            r1 = self.c_left.getPreorder(r1)
        if (self.c_rightid != -1):
            r1 = self.c_right.getPreorder(r1)
        return r1       
    def getInorder(self,r1):
        if (self.c_leftid != -1):
            r1 = self.c_left.getInorder(r1)
        r1.append(self.nodeid)
        if (self.c_rightid != -1):
            r1 = self.c_right.getInorder(r1)
        return r1       
    def getPostorder(self,r1):
        if (self.c_leftid != -1):
            r1 = self.c_left.getPostorder(r1)
        if (self.c_rightid != -1):
            r1 = self.c_right.getPostorder(r1)
        r1.append(self.nodeid)
        return r1       
    def getRoot(self):
        if (self.parentid == -1):
            return self
        return self.parent.getRoot()


    def showNode(self):
        i1 = self.nodeid
        i2 = self.parentid
        i3 = self.getSibling()
        i4 = self.getDegree()
        i5 = self.getDepth()
        i6 = self.getHeight()
        i7 = self.getNodeType()
        print ('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(i1,i2,i3,i4,i5,i6,i7))
        return



#analysis
n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l1.insert(0,-1)
l1.append(-1)
l2.insert(0,-1)
l2.append(-1)
l3 = copy.deepcopy(l2)


ilist = []
for i in range(1,n+1):
    tmp = []
    for j in range(1,n+1):
        if (l1[i] == l2[j]):
            l3[j] = -1
            tmp.append(l1[i])

            t2 = []
            for v in range(j-1,0,-1):
                if (l3[v] == -1 ):
                    break
                t2.append(v)
            if (len(t2) > 0):
                tmp.append(l1[i+1])
                for k in range(1,n + 1):
                    if (l3[k] == l1[i+1]):
                        l3[k] = -1
            else:
                tmp.append(-1)

            t1 = []
            for v in range(j+1,n+1):
                if (l3[v] == -1 ):
                    break
                t1.append(v)

            if (len(t1) > 0):
                tmp.append(l1[i+len(t2)+1])
                for k in range(1,n + 1):
                    if (l3[k] == l1[i+len(t2)+1]):
                        l3[k] = -1
            else:
                tmp.append(-1)
            ilist.append(tmp)


#make node
nl = []
for i in range(0,n+1):
    nl.append(node(i))

for t in ilist:
    (a,b,c) = map(int,t)
    if (b != -1):
        nl[a].setLeftChild(nl[b])
    if (c != -1):
        nl[a].setRightChild(nl[c])
#    print(a,b,c)

root = nl[1].getRoot()
r1 = []
r2 = []
r3 = []
r1 = root.getPreorder(r1)
r2 = root.getInorder(r2)
r3 = root.getPostorder(r3)

#print ("Preorder")
#print ('',' '.join(map(str,r1)))
#print ("Inorder")
#print ('',' '.join(map(str,r2)))
#print ("Postorder")
print (' '.join(map(str,r3)))

