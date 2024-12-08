# list = [5, 8, 0, 4, 11, 0, 6, 9]
#
# for item in list:
#     if item == 0:
#         list.remove(item)
#         list.append(item)
#
# print(list)
#
# number: int = 500
# print (number >> 1)
#
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print (i)
#     i += 1
#
# lower = 5
# upper = 120
# print("Prime number between", lower, "and", upper, "are")
#
# for num in range(lower, upper + 1): #all prime numbers are grater than 1
#     if num > 1:
#         for i in range(2, num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)

'''
rng = range(2, 10, 2)
print(list(rng))
print(type(list))

### built-in len function below

tasks = ["write code", "test", "debug", "fix", "ship"]

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}. {task}")

### built-in zip function below

name = ["mike", "jen", "ken", "lily"]
age = [45, 32, 36, 21]
gender = ["male", "female", "male"]

combined = list(zip(name, age, gender))
print (combined)

for name, age, gender in combined:
    print(f"{name} is {age} years old and is {gender}")

# birth_year = input("enter birth_year: " )
# age = 2019 - int(birth_year)
# print(age)

## covert weight lbs into kg from your input
your_weight = input("enter your weight in lbs: ")
weight = int(your_weight) * .45359
text = 'i think i got it, Function vs method'

f-string syntax: Everything inside {} gets evaluated.
The f before the string allows variable interpolation.
Precision formatting: {weight:.2f} limits the output to 2 decimal places
for better readability.

print(f"You weigh {weight:.2f} kg.")
print('weight' in  your_weight) # in operator is ude to return boolean value, True or False
print(text.title())
'''
from xml.dom.minidom import ProcessingInstruction

# Arithmatic operations

# print (10 // 3) # to remove decimal, return 3
# print (10 ** 3) # exponential operator, returns 10x10x10=1000
# x = 10
# x += 3 #augmented assignment operator, 10 + 3
# print(x)
#x = 10 + 3 * 2 ** 2
# x = (10 + 3) ** 2 * 2 # order is parenthesis, exponentiation, multi, div, add, sub
# print(x)
# y = -2.9
# print(abs(y))

#Conditions

# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
# elif is_cold:
#     print("It's a cold day")
# else:
#     print("Have a lovely day!")

# While loop

# num = 1
# while num <= 10:
#     print(num)
#     num += 2 # incremented by 2 with 1 until reaches 10
# print("Done!")

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

#print a triangle
def print_triangle(n):
    for i in range(1, n+1):
        print("*" * i)
print_triangle(10)
