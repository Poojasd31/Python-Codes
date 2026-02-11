#18-10-24

#Iterative Statement-> While Loop
# String Formatting

#Iterative Statement-> It will give us Iterative statement
#Iterative statement=> for loop and while loop

'''For Loop'''
#for var in iterable:
  #statement

'''While Loop'''
#It is also loop

#ICU=> Initializations, Condition and Update

# initialization
# while Condition:
#     #statement
#     Update

#after while put a condition
"""If ur condition is true then while loop will start and 
if condition is false then while loop will stop"""

# i=1
# while i<5:
#     print(i)
#     i=i+1
# print("coding.....")
# 1
# 2
# 3
# 4
#coding.....

#WAP TO PRINT NUMBERS FROM 11-20 NBY USING WHILE LOOP



# i=11

# while i<=20 :
#     print(i)
#     i=i+1
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

#Wap to print even numbers from 11-20 by using while loop

# num = 12

# while num<=20:
#     print(num)
#     num=num+2
# 12
# 14
# 16
# 18
# 20

#WAP to print numbers from 100-90 by using while loop

# num = 100
# while num>=90:
#     print(num)
#     num=num-1

#100
# 99
# 98
# 97
# 96
# 95
# 94
# 93
# 92
# 91
# 90

'''
While loop
#Group of statement

'''
#WAP to print list of name of 5 students

# student=[]
# i=1
# while i<=5:
#     name=input("Enter name=>")
#     student.append(name)
#     i=i+1
# print(student)

# Enter name=>Pooja
# Enter name=>Rohit
# Enter name=>Mohit
# Enter name=>Raavi
# Enter name=>Sita
# ['Pooja', 'Rohit', 'Mohit', 'Raavi', 'Sita']

#WAP To iterate elements from list by using while loop

# student=['nilesh','lalit','yogesh','jay','veeru']

# name = 0

# while name<5:
#     print(student[name])
#     name = name + 1

# nilesh
# lalit
# yogesh
# jay
# veeru

#Calculator
# while True:
#   num1=eval(input("ENTER NUMBER 1=>"))
#   op=str(input("ENTER OPERATOR=>"))
#   num2=eval(input("ENTER NUMBER 2=>"))

#   if op=="+":
#     print(num1+num2)

#   elif op=="-":
#     print(num1-num2)

#   elif op=="/":
#     print(num1+num2)

#   elif op=="*":
#     print(num1+num2)
   
#   else:
#     print("Invalid Operator")

'''Transfer Statement'''
#pass
#continue
#break

'''IF, ELIF, ELSE AND FOR Have BLOCK'''

#PASS
'''
It is keyword, we used when we want to keep block empty.
It is a placeholder it will run a code without causing an error
'''

#CONTINUE
'''
IT is eterative statement, It will stop/skip current iteration

'''
# l=[11,2,33,66,12]

# for i in l:
#     continue
#     print(i)



# l=[1,2,3,4,5,6,7,8]

# for num in l:
#    if num%2!=0:
#     continue
#    print(num)
# 2
# 4
# 6
# 8

#WAP to remove all white space from string
'''
course="python programming language"
#output:
pythonprogramminglangguage
'''
# course="python programming language"

# out=" "

# for char in course:
#     if char !=" ":
#      out=out+char
# print(out)
#pythonprogramminglanguage

#BREAK
'''
Break used when we want to stop the loop
'''

# l=[11,22,33,44,55]

# for i in l:
#    if i ==33:
#     break
#    print(i)
# #11
# #22

# # Calculator
# while True:
#   num1=eval(input("ENTER NUMBER 1=>"))
#   op=str(input("ENTER OPERATOR=>"))
#   num2=eval(input("ENTER NUMBER 2=>"))

#   if op=="+":
#     print(num1+num2)

#   elif op=="-":
#     print(num1-num2)

#   elif op=="/":
#     print(num1+num2)

#   elif op=="*":
#     print(num1+num2)
   
#   else:
#     print("Invalid Operator")

#   ch=input("Do you wat to continue=>")
#   if ch=="No":
#     break

name="The Kiran Academy"

char=0

while char<len(name):
    print(name[char])
    char=char+1

# T
# h
# e

# K
# i
# r
# a
# n

# A
# c
# a
# d
# e
# m
# y