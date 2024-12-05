class Box:
    def __init__(self,status=0,draw = "|_|"):
        self.status = status
        self.draw = draw

    def boxtaken(self):
        if self.status == 0:
            return False
        else:
            print("this box is taken!")
            return True
    
    def take(self,player):
        if player == True:
            self.status = 1
            self.draw = "|X|"
        elif player == False:
            self.status = 2
            self.draw = "|O|"

    def move(self,player):
        if self.boxtaken() == False:
            self.take(player)
        elif self.boxtaken() == True:
            print("velg en ny box")

box1=Box()
box2=Box()
box3=Box()
box4=Box()
box5=Box()
box6=Box()
box7=Box()
box8=Box()
box9=Box()

def showBoard():
    print("\n",box1.draw + box2.draw + box3.draw,"\n",box4.draw + box5.draw + box6.draw,"\n",box7.draw + box8.draw + box9.draw)


