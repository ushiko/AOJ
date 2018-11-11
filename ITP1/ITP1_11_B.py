

class Dice:
    diceNum = []
    pos = 0
    def setNum(self,i):
        self.pos = i[0]
        self.diceNum.append(i[0])
        self.diceNum.append(i[1])
        self.diceNum.append(i[2])
        self.diceNum.append(i[3])
        self.diceNum.append(i[4])
        self.diceNum.append(i[5])
    def getTopPos(self):
        return self.diceNum[0]    
    def moveToTopnum(self,n):
        i = 0
        for i in range(0,4):
            if (self.getTopPos() == n ):
                return True
            self.move("S")
        else:
            for j in range(0,4):
                if (self.getTopPos() == n ):
                    return True
        return False
    def getFrontPos(self):
        return self.diceNum[1]
    def getRightPos(self):
        return self.diceNum[2]
    def yokoRotate(self):
            i0=self.diceNum[0]
            i1=self.diceNum[2] 
            i2=self.diceNum[4] 
            i3=self.diceNum[1]
            i4=self.diceNum[3]
            i5=self.diceNum[5]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
    def move(self,d):
        if (d == "E"):
            i0=self.diceNum[3]
            i1=self.diceNum[1] 
            i2=self.diceNum[0] 
            i3=self.diceNum[5]
            i4=self.diceNum[4]
            i5=self.diceNum[2]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
        if (d == "W"):
            i0=self.diceNum[2]
            i1=self.diceNum[1] 
            i2=self.diceNum[5] 
            i3=self.diceNum[0]
            i4=self.diceNum[4]
            i5=self.diceNum[3]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
        if (d == "S"):
            i0=self.diceNum[4]
            i1=self.diceNum[0] 
            i2=self.diceNum[2] 
            i3=self.diceNum[3]
            i4=self.diceNum[5]
            i5=self.diceNum[1]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
        if (d == "N"):
            i0=self.diceNum[1]
            i1=self.diceNum[5] 
            i2=self.diceNum[2] 
            i3=self.diceNum[3]
            i4=self.diceNum[0]
            i5=self.diceNum[4]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
    def rotateToFrontnum(self,n):
        for i in range(0,4):
            self.yokoRotate()
            if ( self.getFrontPos() == n):
                return True
            print (self.diceNum)
        return False
 
 
l = list(map(int,input().split()))
dice = Dice()
dice.setNum(l)

n = int(input())
while (n > 0):
    n = n -1
    (t,f) = map(int,input().split())
    dice.moveToTopnum(t)
    dice.rotateToFrontnum(f)
    print (dice.getRightPos())

