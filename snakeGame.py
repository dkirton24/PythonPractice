import turtle
import random

class Square:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.side = 25
        self.penSize = 2
        self.color = ""
        self.isFood = False

    def setXandY(self, isFood):
        if isFood:
            self.x = random.randint(-275, 275)
            self.y = random.randint(-275, 275)
        
            
    
    def setSquareAttributes(self, isFood):
        turtle.pensize(self.penSize)
        if isFood:
            self.color = "red"
            turtle.fillcolor(self.color)
        else:
            self.color = "green"
            turtle.fillcolor(self.color)
            
    def drawSquare(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        
        turtle.begin_fill()
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.left(90)
        turtle.forward(self.side)
        turtle.end_fill()


class Screen:
    def __init__(self):
        self.square = Square()
        
    def drawInitialSquares(self):
        self.square.setXandY(True)
        self.square.setSquareAttributes(True)
        turtle.penup()
        self.square.drawSquare()
        turtle.pendown()

        self.square.setSquareAttributes(False)
        self.square.x = 0
        self.square.y = 0
        turtle.penup()
        self.square.drawSquare()
        turtle.pendown()

    def setScreenProperties(self):
        turtle.setup(600, 600)

    

def main():
    screen = Screen()
    screen.setScreenProperties()
    screen.drawInitialSquares()


main()














