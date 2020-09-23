from numpy import random
class Ghost(object):
    def __init__(self, color=None):
        if color is None:
            color = random.randint(1, 5)
            if(color==1):
                self.color="white"
            elif(color==2):
                self.color="yellow"
            elif(color==3):
                self.color="purple"
            elif(color==4):
                self.color="red"