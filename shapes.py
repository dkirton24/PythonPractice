def main():
    shape = [[], [], [], [], []]
    shape = FillList(shape)
    ##printList(shape)



def FillList(list1):
    count = 1
    for row in range(0, 5):
        for col in range(0, count):
            list1[row].append("$")
            print(list1)
        count+=1
    return list1

def printList(list1):
    count = 1
    for row in range(0, 5):
        for col in range(0, count):
            print(list1[row][col], end="  ")
        print("\n")
        count+=1


main()
