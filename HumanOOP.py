class Human:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.placeOfBirth = ""

    def Birthday(self):
        print("Happy Birthday")
        self.age += 1

    def setPlaceOfBirth(self, placeOfBirth):
        self.placeOfBirth = placeOfBirth

    def PrintDescription(self):
        print("Description of this human")
        print("Name:\t", self.firstName, self.lastName)
        print("Age:\t", self.age)
        print("Place Of Birth:\t", self.placeOfBirth)

class Sandwich:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.ingrediantsList = []

    def buildSandwich(self):
        ingrediant = input("Enter the first ingrediant you want the sandwich: ")
        while ingrediant != "done":
            self.ingrediantsList.append(ingrediant)
            ingrediant = input("Enter the next ingrediant that makes up the sandwich(Enter done if finished): ")

    def getCost(self):
        return self.cost


def main():
    

























    
    
