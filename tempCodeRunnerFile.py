#
for j in range(1, 6):
        print("*", end=" ")
        print()
print("-----------")
    
#53. Write a program to print the pattern 1, 12, 123, 1234, 12345. 
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print("----------------")
   
#54. Write a program using nested loops to print three rows of numbers from 1 to 3. 
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()
print("-------------")
    
#55. Write a program to print multiplication tables from 1 to 3 using nested loops. 
for num in range(1, 4):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print()
print("------------")

#56. Write a program using nested loops to print every student with every mark. 
students = ["Amit", "Rakesh", "Priya"]

marks = [80, 90, 75]

for student in students:
    for mark in marks:
        print(student, mark)
print("----------------")

#57. Write a program using nested loops to print every student with every subject.
students = ["Amit", "Rakesh", "Priya"]
subjects = ["Python", "Java", "SQL"]
for student in students:
    for subject in subjects:
        print(student, subject) 
print("-------------")

#58. Write a program using nested loops to print a 3 × 5 number pattern. 
for i in range(3):
    for j in range(1, 6):
        print(j, end=" ")
    print()
print("------------------")

#59. Write a program using nested loops to print a 5 × 5 star pattern. 
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
print("---------------")

#60. Write a program to print the pattern 5 stars, 4 stars, 3 stars, 2 stars, 1 star
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print("---------------")

#61. Create a function named greeting() that prints "Hello Python". 
def greeting():
    print("Hello python")
greeting()    
print("-------------")

#62. Create a function that accepts a person's name and prints the name. 
def person_name(name):
    print(name)
person_name("Mayuri")
print("-------------")

#63. Create a function that accepts two numbers and prints their addition. 
def addition(a, b):
    print(a+b)
addition(10,20)    
print("--------------")

#64. Create a function that accepts two numbers and prints their subtraction. 
def subtraction(a, b):
    print(a-b)
subtraction(20,10)       
print("-------------")

#65. Create a function that accepts two numbers and prints their multiplication. 
def multiplication(a, b):
    print(a * b)
multiplication(50,50)    
print("-------------")

#66. Create a function that accepts two numbers and prints their division. 
def division(a, b):
    print(a/b)
division(52, 2)    
print("-------------")

#67. Create a function that accepts a number and prints whether it is even or odd. 
def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
even_odd(6)        
print("--------------")

#68. Create a function that accepts a number and prints its multiplication table. 
def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
table(5)
print("-------------")

#69. Create a function that accepts a number and returns its square. 
def square(num):
    return num * num
result = square(5)
print(result)
print("-------------")

#70. Create a function that accepts a number and returns its cube. 
def cube(num):
    return num * num * num
resuly = cube(3)
print(result) 
print("-------------")

#71. Create a function add() that accepts two numbers and returns their addition. 
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
print("--------------")

#72. Create a function subtract() that accepts two numbers and returns their difference. 
def subtract(a, b):
    return a - b
result = subtract(20, 8)
print(result)
print("-----------------")

#73. Create a function that accepts two numbers and returns the larger number. 
def larger(a, b):
    if a > b:
        return a
    else:
        return b
result = larger(15, 25)
print(result)
print("------------")

#74. Create a function that accepts a number and returns whether it is even or odd. 
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = even_odd(7)
print(result)
print("--------------")

#75. Create a function that accepts a number and returns whether it is positive, negative, or zero. 
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
result = check_number(-5)
print(result)
print("------------------")

#76. Create a function that accepts three numbers and returns the largest number. 
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = largest(10, 25, 15)
print(result)
print("--------------")

#77. Create a function that accepts a number and returns the sum from 1 to that number. 
def sum_numbers(num):
    total = 0
    for i in range(1, num + 1):
        total = total + i
        return total
result = sum_numbers(5)
print(result)
print("---------------")

#78. Create a function that accepts a number and returns its factorial. 
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result
answer = factorial(5)
print(answer)
print("-------------")

#79. Create a function that accepts a string and returns its length. 
def string_length(text):
    return len(text)
result = string_length("Python")
print(result)
print("-------------")

#80. Create a function that accepts a string and returns the number of vowels. 
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count
result = count_vowels("Python Programming")
print(result)
print("-------------")