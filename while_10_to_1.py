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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    