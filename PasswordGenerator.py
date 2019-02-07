import random

class PasswordGenerator:
    def __init__(self):
        self.maxInt = 122
        self.minInt = 33
        self.randomDec = 0
        self.randChr = ""
        self.passwordList = []

    def getRandomInt(self):
        self.randomDec = random.randint(self.minInt, self.maxInt)

    def translateIntToCharacter(self):
        self.randChr = chr(self.randomDec)

    def addCharacterToList(self):
        self.passwordList.append(self.randChr)

    def printList(self):
        for i in range(0, len(self.passwordList)):
            print(self.passwordList[i], end="")
        print()


def main():
    passwordLength = 16
    newPassword = PasswordGenerator()
    for j in range(0,500):
        newPassword.passwordList = []
        for i in range(0, passwordLength):
            newPassword.getRandomInt()
            newPassword.translateIntToCharacter()
            newPassword.addCharacterToList()

        newPassword.printList()

main()
