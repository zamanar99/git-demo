#import math

# user_num = int(input("Upper limit for Prime Number: "))
#
# def is_prime(num):
#     for i range(2, )

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

class Person:
    def __init__(self, name, age):
        self.name = name       # Public attribute
        self._age = age        # Protected attribute
        self.__salary = 50000  # Private attribute

    def get_salary(self):      # Public method to access private attribute
        return self.__salary

# Using encapsulation
p = Person("Alice", 30)
print(p.name)        # Accessible
print(p._age)        # Accessible, but discouraged
print(p.__salary)  # Raises an AttributeError
print(p.get_salary()) # Access via public method