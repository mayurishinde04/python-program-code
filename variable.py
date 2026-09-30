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
