def FillList():
    housePrices = []
    numHouses = int(input("Enter number of houses sold last year: "))
    for house in range(0, numHouses):
        price = int(input("Enter the value of this house: "))
        housePrices.append(price)

    return housePrices

def getAverage(housePrices):
    total = 0
    for house in range(0, len(housePrices)):
        total += housePrices[house]
    average = total / len(housePrices)
    return average

def countAbove(housePrices, average):
    numAbove = 0
    for house in range(0, len(housePrices)):
        if housePrices[house] > average:
            numAbove += 1
    return numAbove


def countBelow(housePrices, average):
    numBelow = 0
    for house in range(0, len(housePrices)):
        if housePrices[house] < average:
            numBelow += 1
    return numBelow

def main():
    housePrices = FillList()
    average = getAverage(housePrices)
    numAbove = countAbove(housePrices, average)
    numBelow = countBelow(housePrices, average)

    print("The average price of the houses sold is:", average)
    print("The number of houses that sold above the average is:", numAbove)
    print("The number of houses that sold below the average is:", numBelow)

main()









    
