#Create a variable name and store your full name in it. Print the value. 
name = "mayuri shinde"
print(name)

print("---------------------")


#Create two variables firstName and lastName. Print them together as a single string. 


name1 = "mayur"
name2 = "shinde"
print(name1,name2)
print("---------------")

#Store "Python Programming" in a variable. Print the first character of the string. 


name="python programing"
print(name[0])
print("----------------")



#Store "Maharashtra" in a variable. Print its length using len(). 

name="Maharashtra"
print(len(name))
print("----------------")


#Store "I love Python" in a variable. Check whether "Python" is present in the string using in and print the result. 

name="I love Python"
print("Python" in name)


#Store "Hello World" in a variable. Print the string using uppercase letters. 

name="Hello World"
print(name.upper())
print("---------------")


#Store "PYTHON PROGRAMMING" in a variable. Print the string using lowercase letters. 

name="PYTHON PROGRAMMIN"
print(name.lower())
print("----------------")


#Store " Hello Python " in a variable. Remove the extra spaces from the beginning and end and print the result. 

name="  Hello Python  "
print(name.strip())
print("----------------")


#Store "Hello Python" in a variable. Replace "Python" with "World" and print the result. 

name=("Hello Python")
print(name.replace("Python","World"))
print("------------------")


# Store "Python Programming" in a variable. Print only "Python" using string slicing. 

name=("Python Programming")
print(name[:6])
print("------------------")


# Store "Maharashtra" in a variable. Print the first 5 characters using slicing. 


name = "Maharashtra"
print(name[:6])
print("----------------")


# Store "Programming" in a variable. Print the last 5 characters using negative indexing/slicing. 

name="Programming"
print(name[-5:])
print("----------------")


# the

x = True
print(type(x))
print("-----------------")


#Write a Python program to check whether a number is between 10 and 100 or equal to 500.

num = int(input("Enter a number: "))

if (num >= 10 and num <= 100) or num == 500:
    print("Number is between 10 and 100 or equal to 500")
else:
    print("Number does not satisfy the condition")
print("----------------")





