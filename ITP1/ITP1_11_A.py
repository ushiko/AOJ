

class Dice:
    diceNum = []
    pos = 0
    def setNum(self,i):
        self.pos = i[0]
        self.diceNum.append(i[0])
        self.diceNum.append(i[2])
        self.diceNum.append(i[5])
        self.diceNum.append(i[3])
        self.diceNum.append(i[4])
        self.diceNum.append(i[1])
    def showPos(self):
        print (self.pos)
    def move(self,d):
        if (d == "E"):
            i0=self.diceNum[3]
            i1=self.diceNum[0] 
            i2=self.diceNum[1] 
            i3=self.diceNum[2]
            i4=self.diceNum[4]
            i5=self.diceNum[5]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
            self.pos = self.diceNum[0]
        if (d == "W"):
            i0=self.diceNum[1]
            i1=self.diceNum[2] 
            i2=self.diceNum[3] 
            i3=self.diceNum[0]
            i4=self.diceNum[4]
            i5=self.diceNum[5]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
            self.pos = self.diceNum[0]
        if (d == "S"):
            i0=self.diceNum[4]
            i1=self.diceNum[1] 
            i2=self.diceNum[5] 
            i3=self.diceNum[3]
            i4=self.diceNum[2]
            i5=self.diceNum[0]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
            self.pos = self.diceNum[0]
        if (d == "N"):
            i0=self.diceNum[5]
            i1=self.diceNum[1] 
            i2=self.diceNum[4] 
            i3=self.diceNum[3]
            i4=self.diceNum[0]
            i5=self.diceNum[2]
            self.diceNum =[i0,i1,i2,i3,i4,i5]
            self.pos= self.diceNum[0]

l = list(map(int,input().split()))
dice = Dice()
dice.setNum(l)
for i in str(input()):
    dice.move(i)
dice.showPos()


