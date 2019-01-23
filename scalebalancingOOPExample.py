import random, sys
class Scale:
    def __init__(self):
        self.leftSide = []
        self.rightSide = []

    def setLists(self):
        for i in range(0, 10):
            self.leftSide.append(random.randint(1,20))
            self.rightSide.append(random.randint(1,20))
    def determineWeight(self):
        
        leftTotal = sum(self.leftSide)
        rightTotal = sum(self.rightSide)

        if leftTotal == rightTotal:
            print("The scales are perfectly balanced!!")
            sys.exit()
        else:
            if leftTotal > rightTotal:
                #print(leftTotal - rightTotal)
                return leftTotal - rightTotal
            elif rightTotal > leftTotal:
                #print(rightTotal - leftTotal)
                return rightTotal - leftTotal

def main():
    while True:
        TestScale = Scale()
        TestScale.setLists()
        print(TestScale.determineWeight())
main()
