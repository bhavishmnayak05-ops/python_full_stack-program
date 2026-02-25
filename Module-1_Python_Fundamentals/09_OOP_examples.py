# 09_OOP_examples.py
from abc import ABC, abstractmethod

# --- 1. Inheritance ---
# Parent class
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Child class (Inherits from Person)
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) # Call parent constructor
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying.")

print("--- Inheritance Example ---")
s = Student("Sriram", "S123")
s.greet()
s.study()

# --- 2. Encapsulation ---
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private variable (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")

    def get_balance(self): # Public method to access private data
        return self.__balance

print("\n--- Encapsulation Example ---")
account = BankAccount("Alice", 1000)
account.deposit(500)
print("Balance:", account.get_balance())
# print(account.__balance) # This would cause an error!

# --- 3. Polymorphism ---
class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

def make_animal_speak(animal):
    print(animal.speak())

print("\n--- Polymorphism Example ---")
make_animal_speak(Cat()) # Same function, different behavior
make_animal_speak(Dog())

# --- 4. Abstraction ---
class Shape(ABC): # Abstract Class
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self): # Must implement abstract method
        return self.side * self.side

print("\n--- Abstraction Example ---")
# s = Shape() # Error! Cannot create object of abstract class
sq = Square(5)
print("Square Area:", sq.area())
