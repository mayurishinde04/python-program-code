#Print numbers from 1 to 20
for i in range(1, 21):
    print(i)
print("-----------------")   
 
#Print numbers from 20 to 1
for i in range(20, 0, -1):
    print(i)
print("-------------------")    

#Print all even numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print("--------------")

# Print all odd numbers from 1 to 50
for i in range(1, 51):
    if i % 2 != 0:
        print(i)
print("--------------")   

#Print the multiplication table of a given number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("-------------")  

#  Find the sum of numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum =", total)
print("-------------------")

#Find the sum of even numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i
print("Sum of even numbers =", total)
print("--------------")

#Find the sum of odd numbers from 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total = total + i
print("Sum of odd numbers =", total)
print("-------------------")

#Find the factorial of a given number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial =", factorial)
print("--------------")

#Count the digits of a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print("Number of digits =", count)
print("----------------")

#Find the sum of digits of a given number
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print("Sum of digits =", total)
print("---------------")

#Find the product of digits of a given number
num = int(input("Enter a number: "))
product = 1
while num > 0:
    digit = num % 10
    product = product * digit
    num = num // 10
print("Product of digits =", product)
print("--------------")

#Reverse a given number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse =", reverse)
print("----------------")

#Check whether a given number is a palindrome
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
print("----------------")   

# Find the largest digit in a given number
num = int(input("Enter a number: "))
largest = 0
while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10
print("Largest digit =", largest)
print("---------------")

#Find the smallest digit in a given number
num = int(input("Enter a number: "))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10
print("Smallest digit =", smallest)
print("---------------")

#Count how many even digits are present in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count = count + 1
    num = num // 10
print("Number of even digits =", count)
print("--------------------")

#Count how many odd digits are present in a given number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count = count + 1
    num = num // 10
print("Number of odd digits =", count)
print("----------------")

#Check whether a given number is divisible by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
print("-------------------") 

#Check whether a given number is divisible by 2
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")
print("-------------")  

#Print all factors of a given number
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
print("-------------------")  

#Find the sum of all factors of a given number.
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num + 1):
    if num % i == 0:
        sum = sum + i
print("Sum of factors:", sum) 
print("-----------------") 

#Check whether a given number is prime.
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
print("--------------") 

#Print prime numbers from 1 to 50.
for num in range(2, 51):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
if count == 2:
        print(num)  
print("------------")
        
# Print the Fibonacci series for n terms.
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c 
print("-------------------")  

#Find the largest number among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest number:", a)
elif b > a and b > c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
print("-------------")    

#Find the smallest number among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b and a < c:
    print("Smallest number:", a)
elif b < a and b < c:
    print("Smallest number:", b)
else:
    print("Smallest number:", c)
print("------------------") 

#Print numbers between two given numbers. 
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for i in range(start, end + 1):
    print(i)          
print("--------------")

#Print all numbers between 1 and 100 that are divisible by 3.
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
print("----------------")

#Print all numbers between 1 and 100 that are divisible by 7.
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
print("------------")        














     