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
        elif player == False:
            self.status = 2

    
    def move(self):
        if self.boxtaken() == False:
            self.take()
        


box1=Box()
box2=Box()
box3=Box()
box4=Box()
box5=Box()
box6=Box()
box7=Box()
box8=Box()
box9=Box()

