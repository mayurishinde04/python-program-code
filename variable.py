#Store "Maharashtra" in a variable. Print its length using len(). 

name="Maharashtra"
print(len(name))
print("----------------")

stdName = ["Chetan", 2, True, 2.5, 1+7j]
print(stdName)
print("----------------")

# list

stdName = list(("Chetan", 2, True, 2.5, 1+7j))
print(stdName)
print("----------------")

#list

stdName = ["Chetan", "Yogesh", "Nilima"]
print(stdName)
print("---------------")

#
fruits = ["Apple", "Mango"]
fruits.append("Banana")
print(fruits)
print("----------------")



#Write a Python program to check whether three numbers are in decreasing order.

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

c = int(input("Enter third number: "))

if a > b and b > c:
    print("Numbers are in decreasing order")
else:
    print("Numbers are not in decreasing order")
print("---------------")

# the    
stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdName[0] = 1
print(stdName)
print("-----------")

#91 Create a function student_info(name, age) and print the student's name and age
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Mayuri", 20)
print("----------------")

#92 Create a function that accepts first name and last name and prints the full name.
def full_name(first_name, last_name):
    print(first_name, last_name)
full_name("Mayuri", "Shinde")
print("--------------")

#93 Create a function that accepts name, age, and city and prints the student information.
def student_info(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
student_info("Mayuri", 20, "Pune")
print("---------------")

#94 Create a function with a default parameter language="Python" and call it with and without an argument.
def programming_language(language="Python"):
    print("Language:", language)
programming_language()
programming_language("Java")
print("---------------")

#95 Create a function greet(name="User") that prints a greeting.
def greet(name="User"):
    print("Hello", name)
greet()
greet("Mayuri")
print("---------------")

#96 Create a function with a default country="India" and print the country
def country_name(country="India"):
    print("Country:", country)
country_name()
country_name("USA")
print("-------------")

#97 Create a function that accepts a number and a default multiplier of 10 and returns the result.
def multiply(number, multiplier=10):
    return number * multiplier
result = multiply(5)
print(result)
print("---------------")

#98 Create a function using *args that prints all the numbers passed to it.
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(10, 20, 30, 40)
print("---------------")

#99 Create a function using *args that calculates the sum of all arguments.
def total_sum(*args):
    total = 0
    for number in args:
        total = total + number
    return total
result = total_sum(10, 20, 30, 40)
print(result)
print("-----------------")

#100 Create a function using *args that finds the largest number
def largest_number(*args):
    largest = args[0]
    for number in args:
        if number > largest:
            largest = number
    return largest
result = largest_number(10, 50, 30, 20, 40)
print(result)
print("----------------")

#101 Create a function using *args that counts how many arguments were passed.
def count_args(*args):
    return len(args)
result = count_args(10, 20, 30, 40, 50)
print(result)
print("--------------")

#102 Create a function using *args that prints each argument on a separate line.
def print_args(*args):
    for value in args:
        print(value)
print_args(10, 20, 30, 40)
print("-----------")

#103 Create a function using *args and calculate the total of 10, 20, 30, 40, and 50.
def total_sum(*args):
    total = 0
    for number in args:
        total = total + number
    return total
result = total_sum(10, 20, 30, 40, 50)
print(result)
print("---------------")

#104 Create a function using **kwargs that prints all student information.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_info(name="Amit", age=21, city="Pune")
print("-----------")

#105 Create a function using **kwargs that prints the name, age, and city
def student_info(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("City:", kwargs["city"])
student_info(name="Amit", age=21, city="Pune")
print("----------------")

#106 Create a function using **kwargs that prints all keys.
def print_keys(**kwargs):
    for key in kwargs:
        print(key)
print_keys(name="Amit", age=21, city="Pune")
print("-------------")

#107 Create a function using **kwargs that prints all values.
def print_values(**kwargs):
    for value in kwargs.values():
        print(value)
print_values(name="Amit", age=21, city="Pune")
print("---------------")

#108 Create a function using **kwargs to display employee information.
def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
employee_info(name="Rahul", age=25, salary=30000, city="Pune")
print("-----------")

#109 Write a function that accepts a number and prints all even numbers from 1 to that number.
def even_numbers(num):
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
even_numbers(10)
print("--------------")

#110. Write a function that accepts a number and returns the sum of all even numbers from 1 to that number.
def sum_even(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total = total + i
    return total
result = sum_even(10)
print(result)
print("-------------") 

#111. Write a function that accepts a number and prints its multiplication table from 1 to 10.
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
multiplication_table(5)
print("---------------")

#112. Write a function that accepts a list and returns the sum of even numbers.
def sum_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total
result = sum_even([10, 15, 20, 25, 30])
print(result)
print("---------------")

#113. Write a function that accepts a list and returns the sum of odd numbers.
def sum_odd(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total = total + num
    return total
result = sum_odd([10, 15, 20, 25, 30])
print(result)
print("-----------------")

#114. Write a function that accepts a list and returns the count of numbers greater than 50.
def count_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 50:
            count = count + 1
    return count
result = count_numbers([20, 60, 75, 30, 90, 45])
print(result)
print("-----------------")

#115. Write a function that accepts a string and counts vowels and consonants.
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
count_vowels_consonants("Python")
print("-------------------")

#116. Write a function that accepts a list of names and searches for a particular name using break.
def search_name(names, target):
    for name in names:
        if name == target:
            print("Name found")
            break
    else:
        print("Name not found")
search_name(["Amit", "Priya", "Rahul", "Sneha"], "Rahul")
print("----------------")

#117. Write a program using a while loop that continuously accepts numbers from the user and stops when the user enters 0.
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print("You entered:", num)
print("---------------")    
    
#118. Write a program using a while loop that keeps asking for a password until the correct password is entered.
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Correct password!")
print("------------")

#119. Write a program using a while loop that accepts numbers until the user enters a negative number and then prints the sum of all positive numbers
total = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total = total + num
print("Sum:", total)
print("----------------")

#120. Write a function that accepts a list of numbers and returns the largest even number from the list.
def largest_even(numbers):
    largest = None
    for num in numbers:
        if num % 2 == 0:
            if largest is None or num > largest:
                largest = num
    return largest
result = largest_even([11, 24, 35, 48, 16, 52, 19])
print(result)
print("------------------")