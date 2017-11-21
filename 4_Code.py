"""Using Python 3.6

Ans for 4th Program
Define a class that has two properties x and y. Add a method to the class that adds x & y. Write a routine that uses this class to add two numbers. Write some test cases to test the addition method in the class"""
class Adder(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def add(self): 
        return self.x + self.y 

# routine 
adder = Adder(1, 2)
print("Use 1st routine:",adder.add())

adder1 = Adder(5,10)
print("Use 2nd routine:",adder1.add())

adder2 = Adder(15,10.6)
print("Use 3rd routine:",adder2.add())
