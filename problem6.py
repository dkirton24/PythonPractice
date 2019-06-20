def largerThanN(userList, n):
    for num in userList:
        if num > n:
            print(num, "is greater than", n)


def FillList():
    userList = []
    userLength = int(input("How many numbers do you have?"))
    for num in range(0, userLength):
        number = int(input("Enter a number: "))
        userList.append(number)

    return userList




def main():
    userList = FillList()
    n = int(input("Enter a number for testing: "))
    largerThanN(userList, n)

main()
