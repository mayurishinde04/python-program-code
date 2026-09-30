#Create a list of 5 student names and print the list. 
students = ["Mayuri", "Priya", "Sneha", "Rahul", "Amit"]
print(students)
print("-------------")

#Create a list of 5 numbers and print the first, third, and last element. 
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])
print("---------------")

#Create a list of 10 numbers and access elements using positive indexing. 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[7])
print(numbers[8])
print(numbers[9])
print("---------------")

#Create a list of 10 numbers and access elements using negative indexing. 
num = [52,51,21,41,62,95,41,42,84,21]
print(num[-1])
print(num[-2])
print(num[-3])
print(num[-4])
print(num[-5])
print(num[-6])
print(num[-7])
print(num[-8])
print(num[-9])
print(num[-10])
print("--------------")

#Create a list of 8 numbers and print the element at index 2. 
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2])
print("---------------")

#Create a list of 8 numbers and print the element at index -2. 
numbers = [10,20,30,40,50,60,70,80]
print(numbers[-2])
print("----------------")

#Create a list of 8 numbers and print elements from index 2 to index 6. 
numbers = [10,20,30,40,50,60,70,80]
print(numbers[2:7])
print("-----------------") 

#Create a list of 10 numbers and print the first 5 elements. 
number =[10,20,30,40,50,60,70,80,90,95]
print(number[:6])
print("-------------")

#Create a list of 10 numbers and print the last 5 elements. 
numbers = [10,20,30,40,50,60,70,80,90,95]
print(numbers[-5:])
print("--------------")

# Create a list of 10 numbers and print every second element using slicing. 
numbers = [10,20,30,40,50,60,70,80,90,95]
print(numbers[0::2])
print("---------------")

# Create a list containing different data types such as string, integer, float, and boolean. my_list = ["Mayuri", 25, 85.5, True]
my_list = ["Mayuri", 25, 85.5, True]
print(my_list)
print("----------------")

# Use len() to find the number of elements in a list. 
numbers = [10, 20, 30, 40, 50]
print(len(numbers))
print("----------------")

#Create a list of fruits and check whether "Mango" exists using the "in" keyword.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

if "Mango" in fruits:
    print("Mango exists in the list")
else:
    print("Mango does not exist in the list")
print("----------------")   

#Create an empty list and add 5 elements using append()
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
print(my_list)
print("---------------")

#Create a list of 5 numbers and update the second element.
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)
print("----------------")

# Create a list of employee names and change the third employee's name. 
list = ["sakshi","yash","mayur","dev","gaytri"]
list[3] = "shravni"
print(list)
print("--------------")

# Create a list of numbers and add a new number at the end using append(). 
number = ["10","20","30","40","50"]
number.append(25)
print(number)
print("-------------") 

# Create a list of numbers and add a new number at a specific position using insert(). 
number = ["10","20","30","40","50"]
number.insert(2,55)
print(number)
print("---------------")

# Create a list of 5 numbers and remove one number using remove().
number = ["10","20","30","40","50"]
number.remove("30")
print(number)
print("---------------")

# Create a list of 5 numbers and remove the last element using pop(). 
number = ["10","20","30","40","50"]
number.pop(-1)
print(number)
print("---------------")

#Create a list of numbers and delete an element using del. 
number = ["10","20","30","40","50"]
del number [3]
print(number)
print("---------------")

# Create two lists and combine them using the + operator. 
num1 = [10,20,30,40,50]
num2 = [60,70,80,90,95]
combined_list = num1 + num2
print(combined_list)
print("----------------")

#Create a list and clear all its elements using clear(). 
list = ["shinde","jadhav","avhad","kale","wagh"]
list.clear()
print(list)
print("--------------")

# Create a list of employee names and sort them alphabetically using sort(). 
employee = ["mayuri","tejal","rajshree","swamini","kajal"]
employee.sort()
print(employee)
print("---------------")

#Create a list of numbers and reverse the list using reverse(). 
numbers=["10","20","30","50","40","60"]
numbers.reverse()
print(numbers)
print("---------------")

# Create a list containing duplicate values and use count() to find how many times a particular value appears. 
numbers = [10, 20, 10, 30, 10, 40, 20]
count = numbers.count(10)
print(count)
print("----------------")

# Create a list of numbers and use index() to find the position of a particular number.
numbers = [10,20,30,40,50,]
position = numbers.index(30)
print(position)
print("----------------")

# Create a list of 10 numbers and find the largest number using max(). 
numbers = [10, 25, 5, 40, 15, 60, 30, 80, 20, 50]
largest = max(numbers)
print(largest)
print("----------------")

# Create a list of 10 numbers and find the smallest number using min(). 
numbers = [10, 25, 5, 40, 15, 60, 30, 80, 20, 50]
largest = min(numbers)
print(largest)
print("----------------")

#Create a list of employee salaries and calculate the total salary using sum(). 
salaries = [25000, 30000, 28000, 35000, 40000]
total_salary = sum(salaries)
print(total_salary)
print("------------------")

#Create a list of numbers and calculate the average using sum() and len(). 
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
count = len(numbers)
average = total / count
print("Average =", average)
print("----------------")

#Create a list of 5 employee salaries and increase each salary individually by 10%.
salaries = [20000, 25000, 30000, 35000, 40000]
salaries[0] = salaries[0] * 1.10
salaries[1] = salaries[1] * 1.10
salaries[2] = salaries[2] * 1.10
salaries[3] = salaries[3] * 1.10
salaries[4] = salaries[4] * 1.10
print(salaries)
print("--------------")

#Create a list of 5 numbers and print the first and last elements. 
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("---------------")

#Create a list of 5 student marks and find the highest and lowest marks.
marks = [85, 72, 90, 65, 78]
highest = max(marks)
lowest = min(marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("----------------")

#Create a list of 5 numbers and find the sum, maximum, and minimum values. 
numbers = [10,20,30,40,50,60,70,80,90]
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
print("Sum:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("------------------")

#Create a list of 5 names and access the first, middle, and last name using indexing.
names = ["shinde","jadhav","avhad","wagh","kale"]
print("First name:", names[0])
print("Middle name:", names[2])
print("Last name:", names[4])
print("----------------")

# Create a tuple containing 5 student names and print the tuple. 
names = ["mayur","prasad","vaibhav","aniket","ravi"]
print(names)
print("--------------")

# Create a tuple containing 5 numbers and print the first, third, and last element. 
number = [5,6,7,4,8]
print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])
print("--------------")

# Create a tuple of 8 numbers and access elements using positive indexing. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[7])
print("-------------")

# Create a tuple of 8 numbers and access elements using negative indexing.
numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5])
print(numbers[-6])
print(numbers[-7])
print(numbers[-8])
print("-------------")

#Create a tuple of 10 numbers and print elements from index 2 to index 7. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 95)
print(numbers[2:8])
print("---------------")

# Create a tuple of 10 numbers and print the first 5 elements. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(numbers[:5])
print("------------")

# Create a tuple of 10 numbers and print the last 5 elements. 
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(numbers[-5:])
print("------------")

#Create a tuple of 10 numbers and print every second element using slicing.
number = [10,20,30,40,50,60,70,80,90,100]
print(number[0::2])
print("-------------")

# Create a tuple containing different data types such as string, integer, float, and boolean. 
data = ("Mayuri", 25, 85.5, True)
print(data)
print("--------------")

# Use len() to find the number of elements in a tuple. 
numbers = (10, 20, 30, 40, 50)
print("Number of elements:", len(numbers))
print("-------------")

# Create a tuple of fruits and check whether "Mango" exists using the "in" keyword. 
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
if "Mango" in fruits:
    print("Mango exists in the tuple")
else:
    print("Mango does not exist in the tuple")
    print("-------------")
    
# Create a tuple with only one item and verify its type using type().
my_tuple = (10,)
print(my_tuple)
print(type(my_tuple))
print("---------------")

#Create a list containing 5 numbers and convert it into a tuple using tuple()
numbers = [10, 20, 30, 40, 50]
my_tuple = tuple(numbers)
print("List:", numbers)
print("Tuple:", my_tuple)
print("------------")

# Create a list of employee names and convert it into a tuple using tuple(). 
employees = ["Rahul", "Priya", "Amit", "Sneha", "Neha"]
employee_tuple = tuple(employees)
print("List:", employees)
print("Tuple:", employee_tuple)
print("-------------")

# Print the converted tuple and check its type using type(). 





















