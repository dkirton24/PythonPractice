import turtle as t
import random as r

class RainDrop:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.length = 15
        self.speed = 10

    ##def setScreen(self):
        

    def getRandomCoordinate(self):
        self.x = r.randint(-295, 295)
        self.y = r.randint(280, 300)

    def createDrop(self):
        self.getRandomCoordinate()
        t.goto(self.x, self.y)
        t.seth(270)
        t.pendown()
        self.y = self.y - self.length
        t.goto(self.x, self.y)
        t.penup()

    def rainDown(self):
        
        if self.y > -290:
            t.seth(270)
            t.penup()
            self.y = self.y - 3
            t.goto(self.x, self.y)
            self.y = self.y - self.length
            t.pendown()
            t.goto(self.x, self.y)
            t.penup()


def main():
    
    t.setup(300,300)
    t.speed("fastest")
    t.ht()
    t.penup()
    t.pensize(2)
    t.pencolor("black")
    
    rainDrops = []
    
    for i in range(0, 10):
        rainDrops.append(RainDrop())

    for i in range(0, 10):
        rainDrops[i].createDrop()
        print(rainDrops[i].x, rainDrops[i].y)
        
    for k in range(0, 20):
        t.clear()
        for j in range(0, 10):
            rainDrops[j].rainDown()
            print(rainDrops[j].x, rainDrops[j].y)


        

main()
        
        
