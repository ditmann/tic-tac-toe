class Box:
    def __init__(self,status=0,draw = "|_|"):
        self.status = status
        self.draw = draw

    def boxtaken(self):
        if self.status == 0:
            self.take(self)
        else:
            print("this box is taken!")
    
    def take(self):
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

def isGameOver():
    boxtaken = 0
    boxing = [box1,box2,box3,box4,box5,box6,box7,box8,box9]
    for boxes in boxing:
        if boxes.status !=0:
            boxtaken += 1
    if boxtaken == 9:
        return True
    else:
        return False

def boxPicked(number):
    if number == 1:
        box1.boxtaken(player)
    elif number == 2:
        box2.boxtaken(player)
    elif number == 3:
        box3.boxtaken(player)
    elif number == 4:
        box4.boxtaken(player)
    elif number == 5:
        box5.boxtaken(player)
    elif number == 6:
        box6.boxtaken(player)
    elif number == 7:
        box7.boxtaken(player)
    elif number == 8:
        box8.boxtaken(player)
    elif number == 9:
        box9.boxtaken(player)



def playerSwap():
    global player
    if player == True:
        player = False
    else:
        player = True

player = True

gameOver = isGameOver()
print("Hellow welcome to tic tac toe!\nhope det best wins")
showBoard()
print("the different boxes in the grid has assigned thesse numbers:")
print("\n|1|.|2|.|3|\n|4|.|5|.|6|\n|7|.|8|.|9|")

while gameOver == False:
    boxPicked(int(input("\nwhat box?")))
    showBoard()
    playerSwap()


