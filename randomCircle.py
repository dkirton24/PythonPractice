import turtle
import random

class Circle:
    def __init__(self):
        self.radius = 0
        self.x = 0
        self.y = 0
        self.penSize = 0
        self.penColor = ""
        self.fillColor = ""
        self.colors = ["pink","purple","teal","gold","maroon","green"]
        self.randomColor = ""
    
    def getRandomColor(self):
        randomIndex = random.randint(0, 5)
        self.randomColor = self.colors[randomIndex]

    def setCircleColor(self):
        self.penColor = self.randomColor
        self.fillColor = self.randomColor

    def setRandomRadius(self):
        self.radius = random.randint(10, 50)

    def setRandomPenSize(self):
        self.penSize = random.randint(1, 10)

    def setRandomPosition(self):
        self.x = random.randint(-400, 400)
        self.y = random.randint(-400, 400)


class Screen:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.rCircle = Circle()
        
    def drawSingleCircle(self):
        
        ##Calling Circle Methods
        self.rCircle.getRandomColor()
        self.rCircle.setCircleColor()
        self.rCircle.setRandomRadius()
        self.rCircle.setRandomPenSize()
        self.rCircle.setRandomPosition()

        #Set Circle Attributes for this object
        turtle.pencolor(self.rCircle.penColor)
        turtle.fillcolor(self.rCircle.fillColor)
        turtle.pensize(self.rCircle.penSize)
        turtle.penup()
        turtle.goto(self.rCircle.x, self.rCircle.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.rCircle.radius)
        turtle.end_fill()

    def drawMultipleCircles(self, numberOfCircles):
        #Set screen size
        turtle.setup(self.width, self.height)
        
        for shape in range(0, numberOfCircles):
            self.drawSingleCircle()

def main():
    screen = Screen()
    screen.drawMultipleCircles(100)


main()














