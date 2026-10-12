#1.Write a program to print numbers from 1 to 10 using a while loop. 
num = 1
while num <= 10:
    print(num)
    num = num + 1
print("------------------")   

#2. Write a program to print numbers from 10 to 1 using a while loop.
num = 10
while num >= 1:
    print(num)
    num = num - 1
print("----------------")
    
#3.Write a program to print all even numbers from 1 to 20 using a while loop. 
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1 
print("------------")   

#4. Write a program to print all odd numbers from 1 to 20 using a while loop.
num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num = num + 1 
print("---------------")   

#5. Write a program to calculate the sum of numbers from 1 to 10 using a while loop. 
num = 1
total = 0
while num <= 10:
    total = total + num
    num = num + 1
print(total) 
print("------------------") 

#6. Write a program to print the multiplication table of a number using a while loop. 
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1
print("-------------")    
#7. Write a program to print numbers from 1 to 50 that are divisible by 5. 
num = 1
while num <= 50:
    if num % 5 == 0:
        print(num)
    num = num + 1
print("------------------")    

#8. Write a program to take a number from the user and print numbers from 1 to that number. 
num = int(input("Enter a number: "))
i = 1
while i <= num:
    print(i)
    i = i + 1
print("--------------")   

#9. Write a program to print numbers from 1 to 20 but skip number 10 using continue. 
num = 1
while num <= 20:
    if num == 10:
        num = num + 1
        continue
        print(num)
    num = num + 1 
print("-------------")   

#10. Write a program to print numbers from 1 to 20 and stop when the number reaches 15 using break.  
num = 1
while num <= 20:
    if num == 15:
        break
    print(num)
    num = num + 1
print("-----------------")  

#11. Write a program to print numbers from 1 to 10 using a for loop.   
for num in range(1, 11):
    print(num)
print("-------------")    

#12. Write a program to print numbers from 10 to 1 using a for loop. 
for num in range(10, 0, -1):
    print(num)
print("------------------")   

#13. Write a program to print all even numbers from 1 to 50. 
for num in range(1, 51):
    if num % 2 == 0:
        print(num)
print("---------------")         

#14. Write a program to print all odd numbers from 1 to 50. 
for num in range(1, 51):
    if num % 2 != 0:
        print(num)
print("----------------") 

#15. Write a program to print the multiplication table of a number using a for loop.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("----------------")   

#16. Write a program to calculate the sum of numbers from 1 to 100. 
total = 0
for num in range(1, 101):
    total = total + num
print(total) 
print("----------------") 

#17. Write a program to print numbers from 1 to 50 with a gap of 2. 
for num in range(1, 51, 2):
    print(num)
print("---------------")   

#18. Write a program to print numbers from 100 to 50 in reverse order. 
for num in range(100, 49, -1):
    print(num)
print("--------------")          

#19. Write a program to print numbers divisible by 3 between 1 and 50. 8
for num in range(1, 51):
    if num % 3 == 0:
        print(num)
print("-------------")

#20. Write a program to print numbers divisible by both 3 and 5 between 1 and 100. 
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
print("----------------")

#21. Write a program to print each character of the string "Python" on a new line. 
text = "Python"
for char in text:
    print(char)
print("------------")

#22. Write a program to count the number of characters in a string using a for loop. 
text = "Python"
count = 0
for char in text:
    count = count + 1
print(count)
print("----------")

#23. Write a program to count the number of vowels in a string. 
text = "Python"
count = 0
for char in text:
    if char in "aeiou":
        count = count + 1
print(count)
print("--------------")

#24. Write a program to count the number of consonants in a string. 
text = "Python"
count = 0
for char in text:
    if char not in "aeiou":
        count = count + 1
print(count)
print("---------------")

#25. Write a program to print only even numbers from a given list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)      
print("----------------")

#26. Write a program to find the sum of all elements in a list. 
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total = total + num
print(total)
print("----------------")

#27. Write a program to find the largest number from a list using a for loop. 
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)
print("-------------")

#28. Write a program to find the smallest number from a list using a for loop. 
numbers = [10, 25, 5, 40, 15]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)
print("------------")

#29. Write a program to print all names from a list. 
names = ["Rakesh", "Amit", "Priya", "Sneha"]
for name in names:
    print(name)
print("---------------") 
   
#30. Write a program to check whether "Rakesh" exists in a given list using a for loop. 
names = ["Amit", "Rakesh", "Priya", "Sneha"]
found = False
for name in names:
    if name == "Rakesh":
        found = True
if found:
    print("Rakesh exists in the list")
else:
    print("Rakesh does not exist in the list")
print("------------")  
  
#31. Write a program to print numbers from 1 to 20 and stop when the number reaches 12. 
for num in range(1, 21):
    if num == 12:
        break
    print(num)
print("---------------") 

#32. Write a program to print numbers from 1 to 20 but skip number 7 using continue. 
for num in range(1,21):   
    if num == 7:
        continue
    print(num)
print("------------") 

#33. Write a program to print all numbers from 1 to 50 except numbers divisible by 5. 
for num in range(1,51):
    if num %5 == 0:
        continue
    print(num)
print("-----------")  

#34. Write a program to search for "Rakesh" in a list. If found, print "Student Found" and stop the loop. 
names = ["Amit", "Priya", "Rakesh", "Sneha"]
for name in names:
    if name == "Rakesh":
        print("Student Found")
        break
print("------------------")  

#35. Write a program to search for a number in a list and stop the loop when the number is found. 
numbers = [10,20,30,40,50] 
for num in numbers:
    if num == 30:
        print("number found") 
        break
print("----------------") 

#36. Write a program to check whether a list contains the number 50 using for-else. 
numbers = [10, 20, 30, 40, 60]
for num in numbers:
    if num == 50:
        print("50 found")
        break
else:
    print("50 not found") 
print("----------------") 

#37. Write a program to search for "Python" in a list of programming languages and print "Python not found" if it does not exist.     
languages = ["Java", "C", "C++", "JavaScript"]
for language in languages:
    if language == "Python":
        print("Python found")
        break
else:
    print("Python not found")
print("--------------------")    

#38. Write a program to print numbers from 1 to 20 and skip all even numbers using continue. 
for num in range(1, 21):
    if num % 2 == 0:
        continue
    print(num)  
print("---------------")

#39. Write a program to print numbers from 1 to 30, skip numbers divisible by 3, and stop when the number reaches 25. 
for num in range(1, 31):
    if num == 25:
        break
    if num % 3 == 0:
        continue
    print(num)  
print("------------") 

#40. Write a program to find the first number greater than 50 in a list and stop the loop. 
numbers = [10, 25, 40, 60, 75, 90]
for num in numbers:
    if num > 50:
        print(num)
        break       
print("--------------") 

#41. Write a program using range() to print numbers 1, 3, 5, 7, 9.    
for num in range(1, 10, 2):
    print(num)
print("----------------") 

#42. Write a program using range() to print numbers 10, 8, 6, 4, 2.        
for num in range(10,1,-2):
    print(num)
print("-------------") 

#43. Write a program to print numbers from 50 to 100 with a gap of 5. 
for num in range(50, 101, 5):      
    print(num)
print("------------------")    
    
#44. Write a program to print numbers from 100 to 50 with a gap of 5. 
for num in range(100, 50, -5):
    print(num) 
print("--------------")       
    
#45. Write a program to print the first 10 multiples of 3. 
for i in range(1, 11):
    print(3 * i)
print("----------------")

#46. Write a program to print the first 10 multiples of 5. 
for i in range (1,11):       
    print(5 * i)
print("-------------") 

#Write a program to print the square of numbers from 1 to 10.   
for num in range(1, 11):
    print(num * num)
print("-------------")        
    
#48. Write a program to print the cube of numbers from 1 to 10.     
for num in range(1,11):    
    print(num * num * num)
print("---------------") 

#49. Write a program to print multiplication tables from 1 to 5. 
for num in range(1, 6):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    print()   
print("--------------")

#50. Write a program to print numbers between 1 and 100 that are divisible by 7.      
for num in range(1, 101):
    if num % 7 == 0:
        print(num)    
print("----------------")

#51. Write a program using nested loops to print numbers from 1 to 3 in rows and columns.
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print() 
print("--------------")    

#52. Write a program using nested loops to print a pattern of 5 stars. 
for i in range(1, 6):
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

