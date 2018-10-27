import Math

def operatorDecision(problem, j):
    if j % 2 == 1:
        #print(problem[j], "odd")
        operand = problem[j]
        if operand == "+":
            total += float(problem[j+1])
            #print(total)
        elif operand == "-":
            total -= float(problem[j+1])
            #print(total)
        elif operand == "*":
            total = total * float(problem[j+1])
            #print(total)
        elif operand == "/":
            total = total / float(problem[j+1])
            #print(total)
        return total
            

def calculator(problem):
    
    
    for i in problem:
        print(i)
    total = float(problem[0])
    for j in range(0,len(problem)):
        total = operatorDecision(problem, j)
    return total
def searchParan(problem):
    paranTotal = 0
    for k in range(0,len(problem)):
        if problem[k].startswith("(") == True:
            startingIndex = k
            startOfP = problem[k][1:]
        elif problem[k].endswith(")") == True:
            endOfP = problem[k][1:]
            endingIndex = k
    for h in range(startingIndex, endingIndex):
        startOfP = float(startOfP)
        endOfP = float(endOfP)
        if h == startingIndex:
            paranTotal += (startOfP + problem[startingIndex])
        elif h > startingIndex and h < endingIndex:
            paranTotal += operatorDecision(problem, h)
        elif h == endingIndex:
            return paranTotal


    

def main():
    print("Welcome to the basic calculator!")
    print("Enter the problem using spaces to seperate:")
    userEnd = False
    problem = input()
    problem = problem.split(" ")
    while userEnd == False:
        total = calculator(problem)
        print("equals: ", total)
        print("Enter another problem or 'end' to stop:")
        problem = input()
        
        if problem == "end" or problem == "End":
            userEnd = True
        else:
            problem = problem.split(" ")


main()












    
