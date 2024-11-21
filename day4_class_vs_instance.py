class Person:
    def __init__(self, initialAge):
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = initialAge

    # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")

    # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1

    def display_age(self):
            print(f"Current age: {self.age}")


initial_age = int(input("Enter the initial age: "))
person = Person(initial_age)

person.amIOld()
person.yearPasses()
person.display_age()
# Increment the age of the person in here


